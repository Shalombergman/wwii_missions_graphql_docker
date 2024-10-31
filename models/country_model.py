


from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index
from sqlalchemy.orm import relationship

from based.base import Base

class CountryModel(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True)
    name = Column(String)

    cities = relationship('CityModel', back_populates='country')