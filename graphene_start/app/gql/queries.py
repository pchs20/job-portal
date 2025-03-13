from graphene import List, ObjectType

from app.database.init_db import employers_data, jobs_data
from app.gql import EmployerObject, JobObject


class Query(ObjectType):
    jobs = List(JobObject)
    employers = List(EmployerObject)

    @staticmethod
    def resolve_jobs(root, info):
        return jobs_data

    @staticmethod
    def resolve_employers(root, info):
        return employers_data
