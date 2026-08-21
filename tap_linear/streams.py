"""Stream type classes for tap-linear."""

from typing import Optional

from tap_linear.client import LinearStream
from tap_linear.queries.comments import commentsQuery
from tap_linear.queries.cycles import cyclesQuery
from tap_linear.queries.initiatives import initiativesQuery
from tap_linear.queries.issue_labels import issueLabelsQuery
from tap_linear.queries.issues import issuesQuery
from tap_linear.queries.project_milestones import projectMilestonesQuery
from tap_linear.queries.project_updates import projectUpdatesQuery
from tap_linear.queries.projects import projectsQuery
from tap_linear.queries.teams import teamsQuery
from tap_linear.queries.users import usersQuery
from tap_linear.queries.workflow_states import workflowStatesQuery
from tap_linear.schemas.comments import commentsSchema
from tap_linear.schemas.cycles import cyclesSchema
from tap_linear.schemas.initiatives import initiativesSchema
from tap_linear.schemas.issue_labels import issueLabelsSchema
from tap_linear.schemas.issues import issuesSchema
from tap_linear.schemas.project_milestones import projectMilestonesSchema
from tap_linear.schemas.project_updates import projectUpdatesSchema
from tap_linear.schemas.projects import projectsSchema
from tap_linear.schemas.teams import teamsSchema
from tap_linear.schemas.users import usersSchema
from tap_linear.schemas.workflow_states import workflowStatesSchema


class IssuesStream(LinearStream):
    """Define the Issues stream."""

    name = "Issues"
    query_name = "issues"
    schema = issuesSchema
    query = issuesQuery

    def post_process(self, row: dict, context: Optional[dict] = None) -> Optional[dict]:
        """Flatten the nested labels connection into a list of labels."""
        row = super().post_process(row, context)
        if row is None:
            return None
        labels = row.get("labels")
        if isinstance(labels, dict):
            row["labels"] = labels.get("nodes", [])
        return row


class TeamsStream(LinearStream):
    """Define the Teams stream."""

    name = "Teams"
    query_name = "teams"
    schema = teamsSchema
    query = teamsQuery


class ProjectsStream(LinearStream):
    """Define the Projects stream."""

    name = "Projects"
    query_name = "projects"
    schema = projectsSchema
    query = projectsQuery


class UsersStream(LinearStream):
    """Define the Users stream."""

    name = "Users"
    query_name = "users"
    schema = usersSchema
    query = usersQuery


class CyclesStream(LinearStream):
    """Define the Cycles stream."""

    name = "Cycles"
    query_name = "cycles"
    schema = cyclesSchema
    query = cyclesQuery


class CommentsStream(LinearStream):
    """Define the Comments stream."""

    name = "Comments"
    query_name = "comments"
    schema = commentsSchema
    query = commentsQuery


class IssueLabelsStream(LinearStream):
    """Define the IssueLabels stream."""

    name = "IssueLabels"
    query_name = "issueLabels"
    schema = issueLabelsSchema
    query = issueLabelsQuery


class WorkflowStatesStream(LinearStream):
    """Define the WorkflowStates stream."""

    name = "WorkflowStates"
    query_name = "workflowStates"
    schema = workflowStatesSchema
    query = workflowStatesQuery


class ProjectMilestonesStream(LinearStream):
    """Define the ProjectMilestones stream."""

    name = "ProjectMilestones"
    query_name = "projectMilestones"
    schema = projectMilestonesSchema
    query = projectMilestonesQuery


class InitiativesStream(LinearStream):
    """Define the Initiatives stream."""

    name = "Initiatives"
    query_name = "initiatives"
    schema = initiativesSchema
    query = initiativesQuery


class ProjectUpdatesStream(LinearStream):
    """Define the ProjectUpdates stream."""

    name = "ProjectUpdates"
    query_name = "projectUpdates"
    schema = projectUpdatesSchema
    query = projectUpdatesQuery
