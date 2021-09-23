from config.databaseConfig import Base

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean

class Client(Base):
    __tablename__ = 'Client'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)