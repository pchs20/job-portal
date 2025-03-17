from graphene import List, ObjectType

from app.deps import get_repository
from app.gql import EmployerObject
from app.respositories import EmployerRepository


class EmployerQuery(ObjectType):
    employers = List(EmployerObject)

    @staticmethod
    async def resolve_employers(root, info):
        employers_repo = await get_repository(EmployerRepository)
        return await employers_repo.get_multi()
