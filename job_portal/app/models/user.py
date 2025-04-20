from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.enums import UserRoleEnum


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String)
    hashed_password = Column(String)
    role = Column(
        Enum(
            UserRoleEnum,
            values_callable=(lambda enum_class: [role.value for role in enum_class]),
        )
    )

    # Relationships
    job_applications = relationship(
        'JobApplication',
        back_populates='user',
        lazy='selectin',
    )
