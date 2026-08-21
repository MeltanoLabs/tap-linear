from singer_sdk import typing as th

from tap_linear.schemas.common import named_ref, user_ref

projectUpdatesSchema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("body", th.StringType),
    th.Property("url", th.StringType),
    th.Property("slugId", th.StringType),
    th.Property("health", th.StringType),
    th.Property("isStale", th.BooleanType),
    th.Property("isDiffHidden", th.BooleanType),
    th.Property("commentCount", th.IntegerType),
    th.Property("diffMarkdown", th.StringType),
    th.Property("editedAt", th.DateTimeType),
    th.Property("createdAt", th.DateTimeType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("archivedAt", th.DateTimeType),
    th.Property("project", named_ref()),
    th.Property("user", user_ref()),
).to_dict()
