#!/usr/bin/python3
"""
db_storage module
The Database storage
"""
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker, Session


class DBStorage:
    """Class that sets up the Database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes instances of the Database class"""
        self.__engine = create_engine(
                "mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db",
                pool_pre_ping=True
                )
        Session = sessionmaker(bind=engine)

    def all(self, cls):
        dictionary = {}
        self.__session = Session()
        if cls is None:
            row = self.__session.query(
                    User, State, City, Amenity, Place, Review).all()
        else:
            row = self.__session.query(cls).all()
        self.__session.close()
        for item in row:
            key = f"{item.__class__.__name__}.{item.id}"
            dictionary[key] = item
        return dictionary

    def new(self, obj):
        self.__session = Session()
        self.__session.add(obj)
        self.session.close()

    def save(self):
        self.__session = Session()
        self.session.commit()
        self.__session.close()

    def delete(self, obj=None):
        self.__session = Session()
        if obj is not None:
            self.__session().delete(obj)
        self.__session.close()
