"""Tests for the Linear streams that do not require API credentials."""

import re

import pytest
import requests_mock

from singer_sdk.exceptions import FatalAPIError

from tap_linear.streams import IssuesStream, TeamsStream
from tap_linear.tap import STREAM_TYPES, TapLinear

SAMPLE_CONFIG = {
    "auth_token": "test-token",
    "start_date": "2024-01-01T00:00:00Z",
}

API_URL = "https://api.linear.app/graphql"


def query_node_fields(query: str) -> set:
    """Return the top-level field names selected inside a query's `nodes` block."""
    body = query[query.index("nodes {") + len("nodes {") :]
    fields = set()
    depth = 1
    for line in body.splitlines():
        line = line.strip()
        if not line:
            continue
        if line == "}":
            depth -= 1
            if depth == 0:
                break
            continue
        if depth == 1:
            fields.add(re.match(r"(\w+)", line).group(1))
        if line.endswith("{"):
            depth += 1
    return fields


def page(query_name: str, nodes: list, has_next: bool = False, cursor=None) -> dict:
    """Build a GraphQL connection response for a stream."""
    return {
        "data": {
            query_name: {
                "pageInfo": {"hasNextPage": has_next, "endCursor": cursor},
                "nodes": nodes,
            }
        }
    }


@pytest.fixture
def tap():
    """Return a tap configured with dummy credentials."""
    return TapLinear(config=SAMPLE_CONFIG)


def build_stream(stream_class, bookmark="2024-01-01T00:00:00Z"):
    """Return a stream ready to request records, as it would be mid-sync."""
    state = {
        "bookmarks": {
            stream_class.name: {
                "replication_key": "updatedAt",
                "replication_key_value": bookmark,
            }
        }
    }
    tap = TapLinear(config=SAMPLE_CONFIG, state=state)
    stream = tap.streams[stream_class.name]
    # A sync resolves the starting replication value from the state (or the
    # start_date) before issuing the first request, so do the same here.
    stream._write_starting_replication_value(None)
    return stream


@pytest.mark.parametrize("stream_class", STREAM_TYPES, ids=lambda c: c.name)
def test_stream_declares_query_and_keys(stream_class, tap):
    """Every stream reads a named connection and replicates on updatedAt."""
    stream = stream_class(tap=tap)
    properties = stream.schema["properties"]

    assert stream.query_name, f"{stream.name} does not set query_name"
    assert f"{stream.query_name}(" in stream.query
    assert stream.primary_keys == ["id"]
    assert stream.replication_key == "updatedAt"
    assert "id" in properties
    assert "updatedAt" in properties


@pytest.mark.parametrize("stream_class", STREAM_TYPES, ids=lambda c: c.name)
def test_query_selection_matches_schema(stream_class, tap):
    """The fields a stream requests are exactly the fields it declares."""
    stream = stream_class(tap=tap)
    assert query_node_fields(stream.query) == set(stream.schema["properties"])


def test_stream_names_are_unique():
    """Stream names must not collide."""
    names = [stream_class.name for stream_class in STREAM_TYPES]
    assert len(names) == len(set(names))


def test_pagination_follows_cursor():
    """Records are read from every page and the cursor is passed forward."""
    stream = build_stream(TeamsStream)
    with requests_mock.Mocker() as mock:
        mock.post(
            API_URL,
            [
                {
                    "json": page(
                        "teams",
                        [{"id": "1", "updatedAt": "2024-02-01T00:00:00Z"}],
                        has_next=True,
                        cursor="cursor-1",
                    )
                },
                {
                    "json": page(
                        "teams", [{"id": "2", "updatedAt": "2024-02-02T00:00:00Z"}]
                    )
                },
            ],
        )
        records = list(stream.get_records(None))

        assert [record["id"] for record in records] == ["1", "2"]
        assert mock.call_count == 2
        assert mock.request_history[0].json()["variables"]["next"] is None
        assert mock.request_history[1].json()["variables"]["next"] == "cursor-1"


def test_request_is_filtered_from_the_bookmark():
    """The replication key value is sent as the filter bound."""
    stream = build_stream(TeamsStream, bookmark="2024-03-04T05:06:07Z")
    with requests_mock.Mocker() as mock:
        mock.post(API_URL, json=page("teams", []))
        list(stream.get_records(None))

        variables = mock.request_history[0].json()["variables"]
        assert variables["replicationKeyValue"].startswith("2024-03-04T05:06:07")


def test_issue_labels_are_flattened(tap):
    """The nested labels connection is flattened to a list of labels."""
    stream = IssuesStream(tap=tap)
    row = {"id": "1", "labels": {"nodes": [{"id": "l1", "name": "bug"}]}}

    assert stream.post_process(row)["labels"] == [{"id": "l1", "name": "bug"}]


def test_issues_without_labels_are_left_alone(tap):
    """An issue with no labels selected passes through untouched."""
    stream = IssuesStream(tap=tap)

    assert stream.post_process({"id": "1"}) == {"id": "1"}


def test_graphql_errors_are_raised():
    """A GraphQL error is surfaced rather than raising a KeyError."""
    stream = build_stream(TeamsStream)
    with requests_mock.Mocker() as mock:
        mock.post(API_URL, json={"errors": [{"message": "Access denied"}]})

        with pytest.raises(FatalAPIError, match="Access denied"):
            list(stream.get_records(None))
