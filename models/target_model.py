from flask import session
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index,Float
from based.base import Base
from sqlalchemy.orm import relationship


class TargetModel(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey('missions.target_id'))
    target_industry = Column(String)
    city_id = Column(Integer, ForeignKey('citys.city_id'))
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'))
    target_priority = Column(Integer)