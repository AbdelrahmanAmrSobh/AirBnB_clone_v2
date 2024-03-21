#!/usr/bin/python3
"""New engine DBStorage"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manges storage of hbnb models in DataBase"""
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine"""
        username = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        dbName = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format
                                      (username, password, host, dbName),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Select from the current database session"""
        result = {}
        classes = {"User": User, "Place": Place, "State": State, "City": City,
                   "Amenity": Amenity, "Review": Review}
        objects = []
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            objects = self.__session.query(cls).all()
        else:
            objects = []
            for key, value in classes.items():
                objects.extend(self.__session.query(value).all())
        for obj in objects:
            result[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return result

    def new(self, obj):
        """Add obj to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj if exist"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                 expire_on_commit=False))
        self.__session = Session()
