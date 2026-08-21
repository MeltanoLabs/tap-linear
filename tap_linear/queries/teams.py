teamsQuery = """
query Teams($next: String, $replicationKeyValue: DateTimeOrDuration) {
    teams(
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
            key
            displayName
            description
            color
            icon
            visibility
            timezone
            createdAt
            updatedAt
            archivedAt
            cyclesEnabled
            cycleDuration
            cycleCooldownTime
            cycleStartDay
            issueEstimationType
            issueEstimationAllowZero
            issueEstimationExtended
            defaultIssueEstimate
            triageEnabled
            autoArchivePeriod
            autoClosePeriod
            parent {
                id
                name
                key
            }
        }
    }
}
"""
