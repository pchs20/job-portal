from graphene import Mutation, ObjectType, String
from graphql import GraphQLError

from app.deps import get_repository
from app.respositories import UserRepository
from app.security import create_access_token


class LoginUser(Mutation):
    class Arguments:
        email = String(required=True)
        password = String(required=True)

    token = String()

    @staticmethod
    async def mutate(root, info, email: str, password: str):
        users_repo = await get_repository(UserRepository)
        user = await users_repo.get_by_email(email=email)
        if user is None:
            raise GraphQLError('Invalid email or password')

        token = create_access_token(email=email)

        return LoginUser(token=token)


class UserMutation(ObjectType):
    login_user = LoginUser.Field()
