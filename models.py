from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin


Base = declarative_base()


class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(), nullable=False, unique=True)
    password = Column(String(), nullable=False)
    email = Column(String(), nullable=False, unique=True)

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
