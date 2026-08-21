projectUpdatesQuery = """
query ProjectUpdates($next: String, $replicationKeyValue: DateTimeOrDuration) {
    projectUpdates(
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
            slugId
            health
            isStale
            isDiffHidden
            commentCount
            diffMarkdown
            editedAt
            createdAt
            updatedAt
            archivedAt
            project {
                id
                name
            }
            user {
                id
                name
                email
            }
        }
    }
}
"""
