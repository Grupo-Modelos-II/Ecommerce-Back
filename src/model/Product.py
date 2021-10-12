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
    mainImage = Column(String(255))

    category = relationship("Category", back_populates="products")
    purchases = relationship("Purchased", back_populates="product")
    images = relationship("Product_Image", back_populates="product")

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
            'name':self.name,
            'amount':self.amount,
            'description':self.description,
            'cost':self.cost,
            'category':self.category,
            'mainImage':self.mainImage,
            'images':self.images,
        }

class Product_Image(Base):
    __tablename__ = 'Product_Image'
    id_product = Column(String(255), ForeignKey('Product.id'), nullable=False, primary_key=True)
    image = Column(String(255), nullable=False, primary_key=True)

    product = relationship("Product", back_populates="images")

    def __init__(self,**kwargs):
        self.id_product = kwargs['id_product']
        self.image = kwargs['image']

    def dict(self):
        return {
            'id_product':self.id_product,
            'image':self.image
        }