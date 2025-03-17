from typing import Any

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


class UpdateJob(Mutation):
    class Arguments:
        job_id = Int(required=True)
        title = String(required=False)
        description = String(required=False)
        employer_id = Int(required=False)

    job = Field(lambda: JobObject)

    @staticmethod
    async def mutate(
        root,
        info,
        job_id,
        title=None,
        description=None,
        employer_id=None,
    ):
        jobs_repo = await get_repository(JobRepository)
        fields_to_update: dict[str, Any] = {}
        if title is not None:
            fields_to_update['title'] = title
        if description is not None:
            fields_to_update['description'] = description
        if employer_id is not None:
            fields_to_update['employer_id'] = employer_id
        job = await jobs_repo.update(job_id, fields_to_update)
        if job is None:
            raise Exception(f'Job with id {job_id} not found')
        return UpdateJob(job=job)


class Mutation(ObjectType):  # type: ignore
    add_job = AddJob.Field()
    update_job = UpdateJob.Field()
