from flask import session
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
class TargetModel(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey('missions.target_id'))
    target_industry = Column(String)
    city_id = Column(Integer, ForeignKey('citys.city_id'))
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'))
    target_priority = Column(Integer)