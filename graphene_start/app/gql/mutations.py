from app.gql.employer import EmployerMutation
from app.gql.job import JobMutation
from app.gql.user import UserMutation


class Mutation(EmployerMutation, JobMutation, UserMutation):  # type: ignore
    pass
