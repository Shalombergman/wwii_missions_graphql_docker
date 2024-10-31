
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index, Float
from sqlalchemy.orm import relationship

from based.base import Base





class CityModel(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    country_id = Column(Integer, ForeignKey('countries.country_id'))
    country = relationship('CountryModel',back_populates='cities')
    targets_city  = relationship('TargetModel', back_populates='city')

