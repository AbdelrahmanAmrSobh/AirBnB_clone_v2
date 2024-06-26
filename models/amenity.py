#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import file_storage_type
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship, backref
from models.place import place_amenity


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    if file_storage_type == "db":
        name = Column(String(128), nullable=True)
        place_amenities = relationship("Place", secondary=place_amenity)
    else:
        name = ""
    
