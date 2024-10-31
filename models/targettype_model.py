from flask import session
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index,Float
from based.base import Base
from sqlalchemy.orm import relationship


class TargetTypeModel(Base):
    __tablename__ = 'targettypes'
    target_type_id = Column(Integer, primary_key=True)
    target_type_name = Column(String)