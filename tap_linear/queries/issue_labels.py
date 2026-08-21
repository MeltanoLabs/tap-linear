issueLabelsQuery = """
query IssueLabels($next: String, $replicationKeyValue: DateTimeOrDuration) {
    issueLabels(
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
            color
            isGroup
            lastAppliedAt
            retiredAt
            createdAt
            updatedAt
            archivedAt
            creator {
                id
                name
                email
            }
            parent {
                id
                name
            }
            team {
                id
                name
                key
            }
        }
    }
}
"""
