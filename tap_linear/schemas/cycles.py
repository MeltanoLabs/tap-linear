from singer_sdk import typing as th

from tap_linear.schemas.common import team_ref

cyclesSchema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("number", th.NumberType),
    th.Property("name", th.StringType),
    th.Property("description", th.StringType),
    th.Property("startsAt", th.DateTimeType),
    th.Property("endsAt", th.DateTimeType),
    th.Property("completedAt", th.DateTimeType),
    th.Property("autoArchivedAt", th.DateTimeType),
    th.Property("progress", th.NumberType),
    th.Property("isActive", th.BooleanType),
    th.Property("isFuture", th.BooleanType),
    th.Property("isNext", th.BooleanType),
    th.Property("isPast", th.BooleanType),
    th.Property("isPrevious", th.BooleanType),
    th.Property("createdAt", th.DateTimeType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("archivedAt", th.DateTimeType),
    th.Property("team", team_ref()),
).to_dict()
