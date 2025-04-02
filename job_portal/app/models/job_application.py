from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database import Base


class JobApplication(Base):
    __tablename__ = 'job_applications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    job_id = Column(Integer, ForeignKey('jobs.id'))

    # Relationships
    user = relationship('User', back_populates='job_applications')
    job = relationship('Job', back_populates='job_applications')
