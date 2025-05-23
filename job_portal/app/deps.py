from functools import wraps
from typing import Type, TypeVar

from graphql import GraphQLError

from app.database import async_session
from app.enums import UserRoleEnum
from app.models import User
from app.respositories import BaseRepository, UserRepository
from app.security import decode_access_token

Repository = TypeVar('Repository', bound=BaseRepository)


async def get_repository(repo_type: Type[Repository]) -> Repository:
    """Factory function to create repository instances."""
    async with async_session() as session:
        return repo_type(session)


async def get_authenticated_user(context) -> User:
    request_obj = context.get('request')
    auth_header = request_obj.headers.get('Authorization')
    if auth_header is None:
        raise GraphQLError('Authorization header not provided')

    # Expected format for Authentication header is: 'Bearer <token>'
    token = auth_header.split(' ')[1]
    payload = decode_access_token(token)

    email = payload.get('sub')
    users_repo = await get_repository(UserRepository)
    user = await users_repo.get_by_email(email=email)
    if user is None:
        raise GraphQLError('Could not authenticate user')
    return user


def admin_user(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Input function always has root and info as first two arguments
        info = args[1]
        user = await get_authenticated_user(info.context)
        if user.role != UserRoleEnum.ADMIN:
            raise GraphQLError('User does not have enough privileges')
        return await func(*args, **kwargs)

    return wrapper


def authenticated_user(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        info = args[1]
        await get_authenticated_user(info.context)
        return await func(*args, **kwargs)

    return wrapper
