projectsQuery = """
query Projects($next: String, $replicationKeyValue: DateTimeOrDuration) {
    projects(
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
            slugId
            identifier
            description
            color
            icon
            priority
            priorityLabel
            progress
            scope
            health
            healthUpdatedAt
            startDate
            targetDate
            sortOrder
            trashed
            url
            createdAt
            updatedAt
            archivedAt
            startedAt
            completedAt
            canceledAt
            autoArchivedAt
            status {
                id
                name
                type
                color
                position
            }
            creator {
                id
                name
                email
            }
            lead {
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
