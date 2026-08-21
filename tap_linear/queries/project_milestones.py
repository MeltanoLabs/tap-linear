projectMilestonesQuery = """
query ProjectMilestones($next: String, $replicationKeyValue: DateTimeOrDuration) {
    projectMilestones(
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
            targetDate
            progress
            sortOrder
            status
            createdAt
            updatedAt
            archivedAt
            project {
                id
                name
            }
        }
    }
}
"""
