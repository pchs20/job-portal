from graphene import Field, Int, Mutation, ObjectType
from graphql import GraphQLError

from app.deps import get_repository
from app.gql import JobApplicationObject
from app.models import JobApplication
from app.respositories import JobApplicationRepository


class ApplyToJob(Mutation):
    class Arguments:
        user_id = Int(required=True)
        job_id = Int(required=True)

    job_application = Field(lambda: JobApplicationObject)

    @staticmethod
    async def mutate(root, info, job_id, user_id):
        job_applications_repo = await get_repository(JobApplicationRepository)
        existing_applications = await job_applications_repo.get_multi(
            job_id=job_id,
            user_id=user_id,
        )
        if existing_applications:
            raise GraphQLError('User has already applied to this job')
        job_application = JobApplication(user_id=user_id, job_id=job_id)
        job_application = await job_applications_repo.create(job_application)
        return ApplyToJob(job_application=job_application)


class JobApplicationMutation(ObjectType):
    apply_to_job = ApplyToJob.Field()
