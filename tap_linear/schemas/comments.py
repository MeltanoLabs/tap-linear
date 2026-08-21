from singer_sdk import typing as th

from tap_linear.schemas.common import issue_ref, user_ref

commentsSchema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("body", th.StringType),
    th.Property("url", th.StringType),
    th.Property("quotedText", th.StringType),
    th.Property("hideInLinear", th.BooleanType),
    th.Property("issueId", th.StringType),
    th.Property("projectId", th.StringType),
    th.Property("projectUpdateId", th.StringType),
    th.Property("initiativeId", th.StringType),
    th.Property("parentId", th.StringType),
    th.Property("resolvingCommentId", th.StringType),
    th.Property("resolvedAt", th.DateTimeType),
    th.Property("editedAt", th.DateTimeType),
    th.Property("createdAt", th.DateTimeType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("archivedAt", th.DateTimeType),
    th.Property("user", user_ref()),
    th.Property("issue", issue_ref()),
    th.Property("resolvingUser", user_ref()),
).to_dict()
