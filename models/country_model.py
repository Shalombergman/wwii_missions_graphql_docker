

from flask import session
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
class Country(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True)
    name = Column(String)