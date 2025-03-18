from graphene import Field, Int, List, ObjectType

from app.deps import get_repository
from app.gql import EmployerObject
from app.respositories import EmployerRepository


class EmployerQuery(ObjectType):
    employers = List(EmployerObject)
    employer = Field(EmployerObject, id=Int(required=True))

    @staticmethod
    async def resolve_employers(root, info):
        employers_repo = await get_repository(EmployerRepository)
        return await employers_repo.get_multi()

    @staticmethod
    async def resolve_employer(root, info, id):
        employers_repo = await get_repository(EmployerRepository)
        employer = await employers_repo.get(id)
        if employer is None:
            raise Exception(f'Employer with id {id} not found')
        return employer
