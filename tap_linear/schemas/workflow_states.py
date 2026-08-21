from singer_sdk import typing as th

from tap_linear.schemas.common import team_ref

workflowStatesSchema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("type", th.StringType),
    th.Property("color", th.StringType),
    th.Property("description", th.StringType),
    th.Property("position", th.NumberType),
    th.Property("createdAt", th.DateTimeType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("archivedAt", th.DateTimeType),
    th.Property("team", team_ref()),
).to_dict()
