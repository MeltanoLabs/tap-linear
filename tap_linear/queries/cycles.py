cyclesQuery = """
query Cycles($next: String, $replicationKeyValue: DateTimeOrDuration) {
    cycles(
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
            number
            name
            description
            startsAt
            endsAt
            completedAt
            autoArchivedAt
            progress
            isActive
            isFuture
            isNext
            isPast
            isPrevious
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
