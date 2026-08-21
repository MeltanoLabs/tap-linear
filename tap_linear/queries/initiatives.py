initiativesQuery = """
query Initiatives($next: String, $replicationKeyValue: DateTimeOrDuration) {
    initiatives(
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
            name
            description
            slugId
            identifier
            icon
            color
            status
            visibility
            health
            healthUpdatedAt
            targetDate
            priority
            sortOrder
            trashed
            url
            createdAt
            updatedAt
            archivedAt
            startedAt
            completedAt
            canceledAt
            creator {
                id
                name
                email
            }
            owner {
                id
                name
                email
            }
            leadTeam {
                id
                name
                key
            }
        }
    }
}
"""
