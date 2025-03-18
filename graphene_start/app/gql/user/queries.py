from graphene import Field, Int, List, ObjectType

from app.deps import get_repository
from app.gql import UserObject
from app.respositories import UserRepository


class UserQuery(ObjectType):
    users = List(UserObject)
    user = Field(UserObject, id=Int(required=True))

    @staticmethod
    async def resolve_users(root, info):
        users_repo = await get_repository(UserRepository)
        return await users_repo.get_multi()

    @staticmethod
    async def resolve_user(root, info, id):
        users_repo = await get_repository(UserRepository)
        user = await users_repo.get(id)
        if user is None:
            raise Exception(f'User with id {user} not found')
        return user
