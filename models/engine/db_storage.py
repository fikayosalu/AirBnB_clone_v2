#!/usr/bin/python3
"""
db_storage module
The Database storage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
import os
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.review import Review
from models.base_model import Base

user = os.getenv('HBNB_MYSQL_USER')
password = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')
env = os.getenv('HBNB_ENV')


class DBStorage:
    """Class that sets up the Database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes instances of the Database class"""
        self.__engine = create_engine(
                f"mysql+mysqldb://{user}:{password}@{host}:3306/{db}",
                pool_pre_ping=True
                )
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the database session all objects depending
        on the class name (argument cls)"""
        dictionary = {}
        if cls is None:
            row = []
            row.extend(self.__session.query(User).all())
            row.extend(self.__session.query(State).all())
            row.extend(self.__session.query(City).all())
            row.extend(self.__session.query(Amenity).all())
            row.extend(self.__session.query(Place).all())
            row.extend(self.__session.query(Review).all())
        else:
            row = self.__session.query(cls).all()
        for item in row:
            key = f"{item.__class__.__name__}.{item.id}"
            dictionary[key] = item
        return dictionary

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not none"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and creates the database session
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
                sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
