"""GraphQL client handling, including LinearStream base class."""

import requests
from typing import Any, Optional, Iterable
from singer_sdk.authenticators import APIKeyAuthenticator
from singer_sdk.exceptions import FatalAPIError
from singer_sdk.streams import GraphQLStream


class LinearStream(GraphQLStream):
    """Linear stream class."""

    # Name of the root connection field this stream reads, e.g. "issues" for the
    # `issues` query. Used to locate the nodes and page info in the response.
    query_name: str = None

    primary_keys = ["id"]
    replication_key = "updatedAt"

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="Authorization",
            value=self.config.get("auth_token"),
            location="header",
        )

    @property
    def url_base(self) -> str:
        return self.config.get("api_url")

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def get_connection(self, response: requests.Response) -> dict:
        """Return this stream's connection object from the response."""
        resp_json = response.json()
        errors = resp_json.get("errors")
        if errors:
            messages = "; ".join(error.get("message", str(error)) for error in errors)
            raise FatalAPIError(f"GraphQL error for stream '{self.name}': {messages}")
        return resp_json["data"][self.query_name]

    def get_next_page_token(
        self, response: requests.models.Response, previous_token: Optional[Any]
    ) -> Any:
        """Return the next page token."""
        page_info = self.get_connection(response)["pageInfo"]
        if page_info["hasNextPage"]:
            return page_info["endCursor"]
        else:
            return None

    def prepare_request_payload(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Optional[dict]:
        """Return the request payload."""
        # The filter is inclusive of the bookmark itself, so the record it came
        # from is re-emitted on the next run rather than risking a gap. Records
        # are upserted on their primary key, so replaying one is harmless.
        value = self.get_starting_timestamp(context).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        self.logger.info(f"Previous state timestamp: {value}")
        body = {
            "query": self.query,
            "variables": {"next": next_page_token, "replicationKeyValue": value},
        }
        return body

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        yield from self.get_connection(response)["nodes"]
