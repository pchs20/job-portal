from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database_config import Base


class Employer(Base):
    __tablename__ = 'employers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_email = Column(String)
    industry = Column(String)

    # Relationships
    jobs = relationship('Job', back_populates='employer')
