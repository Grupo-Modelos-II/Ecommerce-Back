from config.databaseConfig import Base

from uuid import uuid4

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, DateTime, Boolean

class Category(Base):
    __tablename__ = 'Category'
    id = Column(String, primary_key=True)
    name = Column(String(255), nullable=False)

    products = relationship("Product", back_populates="category")

    def __init__(self,**kwargs):
        self.id = str(uuid4())
        self.name = kwargs['name']


    def to_dict(self):
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
    description = Column(String(255), nullable=False)
    cost = Column(BigInteger, nullable=False)

    category = relationship("Category", back_populates="products")
    products_variations = relationship("Product_Variation", back_populates="products")

    def __init__(self,**kwargs):
        self.id = str(uuid4())
        self.id_category = kwargs['id_category']
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.cost = kwargs['cost']

    def to_dict(self):
        return {
            'id':self.id,
            'id_category':self.id_category,
            'name':self.name,
            'description':self.description,
            'cost':self.cost,
            'categories':self.categories,
            'products_variations':self.products_variations
        }

class Product_Variation(Base):
    __tablename__ = 'Product_Variation'
    id = Column(String, primary_key=True)
    id_product = Column(String, ForeignKey('Product.id'), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    cost = Column(BigInteger, nullable=False)

    products = relationship("Product", back_populates="products_variations")
    purchased_variations = relationship("Purchased_Variation", back_populates="products_variations")


    def __init__(self,**kwargs):
        self.id = str(uuid4())
        self.id_product = kwargs['id_product']
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.cost = kwargs['cost']


    def to_dict(self):
        return {
            'id':self.id,
            'id_product':self.id_product,
            'name':self.name,
            'description':self.description,
            'cost':self.cost,
            'products':self.products,
            'purchased_variations':self.purchased_variations
        } 
