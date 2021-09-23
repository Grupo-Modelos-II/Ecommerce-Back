from config.databaseConfig import Base

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean

class Product(Base):
    __tablename__ = 'Product'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))