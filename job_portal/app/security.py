from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from graphql import GraphQLError
from passlib.context import CryptContext

from app.settings import SecuritySettings


settings = SecuritySettings()

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(email: str, expiration_delta: timedelta | None = None) -> str:
    if not expiration_delta:
        expiration_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.now(tz=timezone.utc) + expiration_delta
    to_encode = {
        'sub': email,
        'exp': expire,
    }
    encoded_jwt = jwt.encode(
        payload=to_encode,
        key=settings.SECRET_KEY,
        algorithm=settings.TOKEN_ENCRYPTION_ALGORITHM,
    )
    return encoded_jwt


def decode_access_token(token: str) -> dict[str, Any]:
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.TOKEN_ENCRYPTION_ALGORITHM],
        )
    except jwt.ExpiredSignatureError:
        raise GraphQLError('Token has expired')
    except jwt.InvalidTokenError:
        raise GraphQLError('Invalid token')
    return payload
