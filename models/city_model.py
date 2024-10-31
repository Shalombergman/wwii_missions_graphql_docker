from flask import session
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class CityModel(Base):
    __tablename__ = 'citis'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String)
    latitude = Column(float)
    longitude = Column(float)

    country_id = Column(Integer, ForeignKey('countries.country_id'))