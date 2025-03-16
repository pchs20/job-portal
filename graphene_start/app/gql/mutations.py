from graphene import Field, Int, Mutation, ObjectType, String

from app.deps import get_repository
from app.gql import JobObject
from app.models import Job
from app.respositories import JobRepository


class AddJob(Mutation):
    class Arguments:
        title = String(required=True)
        description = String(required=True)
        employer_id = Int(required=True)

    job = Field(lambda: JobObject)

    @staticmethod
    async def mutate(root, info, title, description, employer_id):
        jobs_repo = await get_repository(JobRepository)
        job = Job(title=title, description=description, employer_id=employer_id)
        job = await jobs_repo.create(job)
        return AddJob(job=job)


class Mutation(ObjectType):  # type: ignore
    add_job = AddJob.Field()
