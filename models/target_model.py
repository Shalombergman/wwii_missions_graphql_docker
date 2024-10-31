
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index,Float
from based.base import Base
from sqlalchemy.orm import relationship


class TargetModel(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True)
    target_priority = Column(Integer)
    target_industry = Column(String)

    mission_id = Column(Integer, ForeignKey('missions.mission_id'))
    mission = relationship('MissionModel', back_populates='targets')


    city_id = Column(Integer, ForeignKey('cities.city_id'))
    city = relationship('CityModel', back_populates='targets_city')

    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'))
    target_type = relationship('TargetTypeModel', back_populates='targets_types')



