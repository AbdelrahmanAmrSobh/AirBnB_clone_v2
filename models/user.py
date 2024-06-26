#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models import file_storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    
    __tablename__ = "users"
    if file_storage_type == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
