

from flask import session
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index
from based.base import Base
from sqlalchemy.orm import relationship

class Country(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True)
    name = Column(String)