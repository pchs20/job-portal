from graphene import Field, Mutation, ObjectType, String
from graphql import GraphQLError

from app.deps import get_authenticated_user, get_repository
from app.enums import UserRoleEnum, UserRoleGrapheneEnum
from app.gql import UserObject
from app.models import User
from app.respositories import UserRepository
from app.security import create_access_token, get_password_hash


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


class AddUser(Mutation):
    class Arguments:
        username = String(required=True)
        email = String(required=True)
        password = String(required=True)
        role = UserRoleGrapheneEnum(required=True)

    user = Field(lambda: UserObject)

    @staticmethod
    async def mutate(
        root,
        info,
        username: str,
        email: str,
        password: str,
        role: UserRoleGrapheneEnum,
    ):
        if role == UserRoleGrapheneEnum.ADMIN:
            current_user = await get_authenticated_user(info.context)
            if current_user.role != UserRoleEnum.ADMIN:
                raise GraphQLError('Only admins can create new admins')
        users_repo = await get_repository(UserRepository)
        if await users_repo.get_by_email(email=email) is not None:
            raise GraphQLError('A user with that email already exists')
        hash_password = get_password_hash(password=password)
        user = User(
            username=username,
            email=email,
            hashed_password=hash_password,
            role=role.value,
        )
        user = await users_repo.create(user)
        return AddUser(user=user)


class UserMutation(ObjectType):
    login_user = LoginUser.Field()
    add_user = AddUser.Field()
