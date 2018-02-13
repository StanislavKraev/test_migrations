from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):

    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(200), nullable=False, index=True)
    surname = Column(String(200), nullable=True, default="")
    password = Column(String(20), nullable=False)


class Session(Base):

    __tablename__ = "session"

    id = Column(BigInteger, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), index=True)
    user = relationship(User, foreign_keys=[user_id])
