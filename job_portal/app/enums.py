from enum import Enum

from graphene import Enum as GrapheneEnum


class UserRoleEnum(str, Enum):
    ADMIN = 'admin'
    EMPLOYER = 'employer'
    APPLICANT = 'applicant'


UserRoleGrapheneEnum = GrapheneEnum.from_enum(UserRoleEnum)
