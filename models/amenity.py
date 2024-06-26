#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import file_storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    if file_storage_type == "db":
        from models.place import place_amenity
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity, back_populates="amenities")
    else:
        name = ""
    
