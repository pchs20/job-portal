from graphene import List, ObjectType

from app.deps import get_repository
from app.gql import JobApplicationObject
from app.respositories import JobApplicationRepository


class JobApplicationQuery(ObjectType):
    job_applications = List(JobApplicationObject)

    @staticmethod
    async def resolve_job_applications(root, info):
        job_applications_repo = await get_repository(JobApplicationRepository)
        return await job_applications_repo.get_multi()
