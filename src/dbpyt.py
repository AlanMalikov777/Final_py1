from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Based = declarative_base()

class Datab(Based):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    login = Column(String())
    password = Column(String())
    token = Column(String())

    def toJSON(self):       
        json = {
            "id":self.id,
            "login":self.login,
            "password":self.password,
            "token":self.token,     
        }

        return json