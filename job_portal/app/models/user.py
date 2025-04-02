from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String)
    hashed_password = Column(String)
    role = Column(String)

    # Relationships
    job_applications = relationship(
        'JobApplication',
        back_populates='user',
        lazy='selectin',
    )
