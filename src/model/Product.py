from config.databaseConfig import Base

from uuid import uuid4

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, DateTime, Boolean

class Category(Base):
    __tablename__ = 'Category'
    id = Column(String, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

    products = relationship("Product", back_populates="category")

    def __init__(self,**kwargs):
        self.id = str(uuid4())
        self.name = kwargs['name']


    def dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'products':self.products
        }

class Product(Base):
    __tablename__ = 'Product'
    id = Column(String, primary_key=True)
    id_category = Column(String, ForeignKey('Category.id'), nullable=False)
    name = Column(String(255), nullable=False)
    amount = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    cost = Column(BigInteger, nullable=False)

    category = relationship("Category", back_populates="products")
    purchases = relationship("Purchased", back_populates="product")

    def __init__(self,**kwargs):
        self.id = str(uuid4())
        self.id_category = kwargs['id_category']
        self.name = kwargs['name']
        self.amount = kwargs['amount']
        self.description = kwargs['description']
        self.cost = kwargs['cost']

    def dict(self):
        return {
            'id':self.id,
            'id_category':self.id_category,
            'name':self.name,
            'amount':self.amount,
            'description':self.description,
            'cost':self.cost,
            'category':self.category
        }