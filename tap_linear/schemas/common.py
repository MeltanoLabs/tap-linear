"""Reference objects shared between Linear stream schemas.

Linear returns related entities inline rather than as foreign keys, so most
streams embed a small subset of the related record. These helpers keep those
embedded shapes consistent across streams.
"""

from singer_sdk import typing as th


def user_ref() -> th.ObjectType:
    """Return the shape used for a related user."""
    return th.ObjectType(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("email", th.StringType),
    )


def team_ref() -> th.ObjectType:
    """Return the shape used for a related team."""
    return th.ObjectType(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("key", th.StringType),
    )


def named_ref() -> th.ObjectType:
    """Return the shape used for a related entity referenced by name."""
    return th.ObjectType(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
    )


def issue_ref() -> th.ObjectType:
    """Return the shape used for a related issue."""
    return th.ObjectType(
        th.Property("id", th.StringType),
        th.Property("identifier", th.StringType),
    )


def cycle_ref() -> th.ObjectType:
    """Return the shape used for a related cycle."""
    return th.ObjectType(
        th.Property("id", th.StringType),
        th.Property("number", th.NumberType),
        th.Property("name", th.StringType),
    )


def state_ref() -> th.ObjectType:
    """Return the shape used for a related workflow state."""
    return th.ObjectType(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("type", th.StringType),
        th.Property("color", th.StringType),
    )


def project_status_ref() -> th.ObjectType:
    """Return the shape used for a related project status."""
    return th.ObjectType(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("type", th.StringType),
        th.Property("color", th.StringType),
        th.Property("position", th.NumberType),
    )


def label_ref() -> th.ObjectType:
    """Return the shape used for a related issue label."""
    return th.ObjectType(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("color", th.StringType),
    )
