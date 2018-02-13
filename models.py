

class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    password = Column(String(10), nullable=False)

