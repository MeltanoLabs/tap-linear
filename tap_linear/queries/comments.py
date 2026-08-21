commentsQuery = """
query Comments($next: String, $replicationKeyValue: DateTimeOrDuration) {
    comments(
        first: 100
        after: $next
        includeArchived: true
        filter: { updatedAt: { gte: $replicationKeyValue } }
    ) {
        pageInfo {
            hasNextPage
            endCursor
        }
        nodes {
            id
            body
            url
            quotedText
            hideInLinear
            issueId
            projectId
            projectUpdateId
            initiativeId
            parentId
            resolvingCommentId
            resolvedAt
            editedAt
            createdAt
            updatedAt
            archivedAt
            user {
                id
                name
                email
            }
            issue {
                id
                identifier
            }
            resolvingUser {
                id
                name
                email
            }
        }
    }
}
"""
