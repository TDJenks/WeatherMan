from sqlalchemy import Column, Integer, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Ability(Base):
    __tablename__ = 'abilities'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default='now()')

    subskills = relationship("Subskill", back_populates="ability", cascade="all, delete-orphan")