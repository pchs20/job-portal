from app.gql.employer import EmployerQuery
from app.gql.job import JobQuery
from app.gql.user import UserQuery


class Query(EmployerQuery, JobQuery, UserQuery):
    pass
