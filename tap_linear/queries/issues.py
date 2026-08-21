issuesQuery = """
query Issues($next: String, $replicationKeyValue: DateTimeOrDuration) {
    issues(
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
            identifier
            number
            title
            description
            url
            branchName
            priority
            priorityLabel
            estimate
            dueDate
            sortOrder
            subIssueSortOrder
            customerTicketCount
            trashed
            createdAt
            updatedAt
            archivedAt
            startedAt
            completedAt
            canceledAt
            autoArchivedAt
            autoClosedAt
            triagedAt
            snoozedUntilAt
            addedToCycleAt
            addedToProjectAt
            addedToTeamAt
            slaStartedAt
            slaBreachesAt
            creator {
                id
                name
                email
            }
            assignee {
                id
                name
                email
            }
            state {
                id
                name
                type
                color
            }
            team {
                id
                name
                key
            }
            project {
                id
                name
            }
            projectMilestone {
                id
                name
            }
            cycle {
                id
                number
                name
            }
            parent {
                id
                identifier
            }
            labels(first: 50) {
                nodes {
                    id
                    name
                    color
                }
            }
        }
    }
}
"""
