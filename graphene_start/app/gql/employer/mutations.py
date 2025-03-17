from graphene import Field, Mutation, ObjectType, String

from app.deps import get_repository
from app.gql import EmployerObject
from app.models import Employer
from app.respositories import EmployerRepository


class AddEmployer(Mutation):
    class Arguments:
        name = String(required=True)
        contact_email = String(required=True)
        industry = String(required=True)

    employer = Field(lambda: EmployerObject)

    @staticmethod
    async def mutate(root, info, name, contact_email, industry):
        employers_repo = await get_repository(EmployerRepository)
        employer = Employer(name=name, contact_email=contact_email, industry=industry)
        employer = await employers_repo.create(employer)
        return AddEmployer(employer=employer)


class EmployerMutation(ObjectType):
    add_employer = AddEmployer.Field()
