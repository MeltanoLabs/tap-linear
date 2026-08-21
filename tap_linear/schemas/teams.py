from singer_sdk import typing as th

from tap_linear.schemas.common import team_ref

teamsSchema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("key", th.StringType),
    th.Property("displayName", th.StringType),
    th.Property("description", th.StringType),
    th.Property("color", th.StringType),
    th.Property("icon", th.StringType),
    th.Property("visibility", th.StringType),
    th.Property("timezone", th.StringType),
    th.Property("createdAt", th.DateTimeType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("archivedAt", th.DateTimeType),
    th.Property("cyclesEnabled", th.BooleanType),
    th.Property("cycleDuration", th.NumberType),
    th.Property("cycleCooldownTime", th.NumberType),
    th.Property("cycleStartDay", th.NumberType),
    th.Property("issueEstimationType", th.StringType),
    th.Property("issueEstimationAllowZero", th.BooleanType),
    th.Property("issueEstimationExtended", th.BooleanType),
    th.Property("defaultIssueEstimate", th.NumberType),
    th.Property("triageEnabled", th.BooleanType),
    th.Property("autoArchivePeriod", th.NumberType),
    th.Property("autoClosePeriod", th.NumberType),
    th.Property("parent", team_ref()),
).to_dict()
