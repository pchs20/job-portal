from graphene import Field, Int, List, ObjectType, String

from app.enums import UserRoleGrapheneEnum


class EmployerObject(ObjectType):
    id = Int()
    name = String()
    contact_email = String()
    industry = String()
    jobs = List(lambda: JobObject)

    @staticmethod
    def resolve_jobs(root, info):
        return root.jobs


class JobObject(ObjectType):
    id = Int()
    title = String()
    description = String()
    employer_id = Int()
    employer = Field(lambda: EmployerObject)
    job_applications = List(lambda: JobApplicationObject)

    @staticmethod
    def resolve_employer(root, info):
        return root.employer


class UserObject(ObjectType):
    id = Int()
    username = String()
    email = String()
    role = UserRoleGrapheneEnum()
    job_applications = List(lambda: JobApplicationObject)

    @staticmethod
    def resolve_user(root, info):
        return root.user


class JobApplicationObject(ObjectType):
    id = Int()
    user_id = Int()
    job_id = Int()
    status = String()
    user = Field(lambda: UserObject)
    job = Field(lambda: JobObject)

    @staticmethod
    def resolve_user(root, info):
        return root.user

    @staticmethod
    def resolve_job(root, info):
        return root.job
