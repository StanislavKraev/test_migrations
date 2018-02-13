from sqlalchemy import Column, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):

    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(200), nullable=False)
    password = Column(String(20), nullable=False)
