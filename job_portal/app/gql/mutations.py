from app.gql.employer import EmployerMutation
from app.gql.job import JobMutation
from app.gql.job_application import JobApplicationMutation
from app.gql.user import UserMutation


class Mutation(
    EmployerMutation,
    JobApplicationMutation,
    JobMutation,
    UserMutation,
):  # type: ignore
    pass
