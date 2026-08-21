from singer_sdk import typing as th

from tap_linear.schemas.common import team_ref, user_ref

initiativesSchema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("description", th.StringType),
    th.Property("slugId", th.StringType),
    th.Property("identifier", th.StringType),
    th.Property("icon", th.StringType),
    th.Property("color", th.StringType),
    th.Property("status", th.StringType),
    th.Property("visibility", th.StringType),
    th.Property("health", th.StringType),
    th.Property("healthUpdatedAt", th.DateTimeType),
    th.Property("targetDate", th.DateType),
    th.Property("priority", th.IntegerType),
    th.Property("sortOrder", th.NumberType),
    th.Property("trashed", th.BooleanType),
    th.Property("url", th.StringType),
    th.Property("createdAt", th.DateTimeType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("archivedAt", th.DateTimeType),
    th.Property("startedAt", th.DateTimeType),
    th.Property("completedAt", th.DateTimeType),
    th.Property("canceledAt", th.DateTimeType),
    th.Property("creator", user_ref()),
    th.Property("owner", user_ref()),
    th.Property("leadTeam", team_ref()),
).to_dict()
