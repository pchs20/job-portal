from app.gql.employer import EmployerQuery
from app.gql.job import JobQuery


class Query(EmployerQuery, JobQuery):
    pass
