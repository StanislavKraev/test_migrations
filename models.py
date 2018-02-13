from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    surname = Column(String(200), nullable=True, default="")
    password = Column(String(20), nullable=False)
