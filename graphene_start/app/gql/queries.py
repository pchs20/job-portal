from graphene import List, ObjectType

from app.deps import get_repository
from app.gql import EmployerObject, JobObject
from app.respositories import EmployerRepository, JobRepository


class Query(ObjectType):
    jobs = List(JobObject)
    employers = List(EmployerObject)

    @staticmethod
    async def resolve_jobs(root, info):
        jobs_repo = await get_repository(JobRepository)
        return await jobs_repo.get_multi()

    @staticmethod
    async def resolve_employers(root, info):
        employers_repo = await get_repository(EmployerRepository)
        return await employers_repo.get_multi()
