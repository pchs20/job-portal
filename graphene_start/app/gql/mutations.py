from app.gql.employer import EmployerMutation
from app.gql.job import JobMutation


class Mutation(EmployerMutation, JobMutation):  # type: ignore
    pass
