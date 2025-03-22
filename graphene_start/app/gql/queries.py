from app.gql.job_application import JobApplicationQuery
from app.gql.employer import EmployerQuery
from app.gql.job import JobQuery
from app.gql.user import UserQuery


class Query(EmployerQuery, JobApplicationQuery, JobQuery, UserQuery):
    pass
