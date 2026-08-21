usersQuery = """
query Users($next: String, $replicationKeyValue: DateTimeOrDuration) {
    users(
        first: 100
        after: $next
        includeArchived: true
        includeDisabled: true
        filter: { updatedAt: { gte: $replicationKeyValue } }
    ) {
        pageInfo {
            hasNextPage
            endCursor
        }
        nodes {
            id
            name
            displayName
            email
            initials
            avatarUrl
            description
            title
            timezone
            active
            admin
            guest
            app
            isAssignable
            isMentionable
            createdIssueCount
            disableReason
            statusEmoji
            statusLabel
            statusUntilAt
            lastSeen
            url
            createdAt
            updatedAt
            archivedAt
        }
    }
}
"""
