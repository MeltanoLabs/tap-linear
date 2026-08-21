from singer_sdk import typing as th

from tap_linear.schemas.common import named_ref

projectMilestonesSchema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("description", th.StringType),
    th.Property("targetDate", th.DateType),
    th.Property("progress", th.NumberType),
    th.Property("sortOrder", th.NumberType),
    th.Property("status", th.StringType),
    th.Property("createdAt", th.DateTimeType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("archivedAt", th.DateTimeType),
    th.Property("project", named_ref()),
).to_dict()
