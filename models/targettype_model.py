
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index,Float
from sqlalchemy.orm import relationship

from based.base import Base



class TargetTypeModel(Base):
    __tablename__ = 'targettypes'
    target_type_id = Column(Integer, primary_key=True)
    target_type_name = Column(String)
    targets_types = relationship('TargetModel', back_populates='target_type')