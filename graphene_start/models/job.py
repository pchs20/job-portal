from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from graphene_start.database_config import Base


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    employer_id = Column(Integer, ForeignKey('employers.id'))

    # Relationships
    employer = relationship('Employer', back_populates='jobs')
