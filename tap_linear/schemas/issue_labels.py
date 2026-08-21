from singer_sdk import typing as th

from tap_linear.schemas.common import named_ref, team_ref, user_ref

issueLabelsSchema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("description", th.StringType),
    th.Property("color", th.StringType),
    th.Property("isGroup", th.BooleanType),
    th.Property("lastAppliedAt", th.DateTimeType),
    th.Property("retiredAt", th.DateTimeType),
    th.Property("createdAt", th.DateTimeType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("archivedAt", th.DateTimeType),
    th.Property("creator", user_ref()),
    th.Property("parent", named_ref()),
    th.Property("team", team_ref()),
).to_dict()
