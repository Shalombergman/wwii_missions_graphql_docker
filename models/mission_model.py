from flask import session
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index,Float
from based.base import Base
from sqlalchemy.orm import relationship


class MissionModel(Base):
    __tablename__ = 'missions'
    id = Column(Integer, primary_key=True)
    mission_date = Column(Date)
    airborne_aircrat = Column(Float)
    attacking_aircrat = Column(Float)
    bomding_aircrat = Column(Float)
    aircraft_returned = Column(Float)
    aircraft_failed = Column(Float)
    aircraft_damaged = Column(Float)
    aircraft_lost = Column(Float)