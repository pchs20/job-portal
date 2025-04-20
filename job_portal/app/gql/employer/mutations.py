from typing import Any

from graphene import Boolean, Field, Int, Mutation, ObjectType, String

from app.deps import admin_user, get_repository
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
    @admin_user
    async def mutate(root, info, name, contact_email, industry):
        employers_repo = await get_repository(EmployerRepository)
        employer = Employer(name=name, contact_email=contact_email, industry=industry)
        employer = await employers_repo.create(employer)
        return AddEmployer(employer=employer)


class UpdateEmployer(Mutation):
    class Arguments:
        employer_id = Int(required=True)
        name = String(required=False)
        contact_email = String(required=False)
        industry = String(required=False)

    employer = Field(lambda: EmployerObject)

    @staticmethod
    async def mutate(
        root,
        info,
        employer_id,
        name=None,
        contact_email=None,
        industry=None,
    ):
        employers_repo = await get_repository(EmployerRepository)
        fields_to_update: dict[str, Any] = {}
        if name is not None:
            fields_to_update['name'] = name
        if contact_email is not None:
            fields_to_update['contact_email'] = contact_email
        if industry is not None:
            fields_to_update['industry'] = industry
        employer = await employers_repo.update(employer_id, fields_to_update)
        if employer is None:
            raise Exception(f'Employer with id {employer_id} not found')
        return UpdateEmployer(employer=employer)


class DeleteEmployer(Mutation):
    class Arguments:
        employer_id = Int(required=True)

    success = Boolean()

    @staticmethod
    @admin_user
    async def mutate(root, info, employer_id):
        employers_repo = await get_repository(EmployerRepository)
        employer = await employers_repo.get(employer_id)
        if employer is None:
            raise Exception(f'Employer with id {employer_id} not found')
        await employers_repo.delete(employer_id)
        return DeleteEmployer(success=True)


class EmployerMutation(ObjectType):
    add_employer = AddEmployer.Field()
    update_employer = UpdateEmployer.Field()
    delete_employer = DeleteEmployer.Field()
