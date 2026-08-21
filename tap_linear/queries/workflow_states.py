workflowStatesQuery = """
query WorkflowStates($next: String, $replicationKeyValue: DateTimeOrDuration) {
    workflowStates(
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
            type
            color
            description
            position
            createdAt
            updatedAt
            archivedAt
            team {
                id
                name
                key
            }
        }
    }
}
"""
