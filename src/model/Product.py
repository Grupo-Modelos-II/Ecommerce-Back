from config.databaseConfig import Base

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, DateTime, Boolean

class Category(Base):
    __tablename__ = 'Category'
    id = Column(String, primary_key=True)
    name = Column(String(255), nullable=False)

    products = relationship("Product", back_populates="categories")

class Product(Base):
    __tablename__ = 'Product'
    id = Column(String, primary_key=True)
    id_category = Column(String, ForeignKey('Category.id'), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    cost = Column(BigInteger, nullable=False)
    has_variations = Column(Boolean, nullable=False, default=False)

    categories = relationship("Category", back_populates="products")
    products_variations = relationship("Product_Variation", back_populates="products")

class Product_Variation(Base):
    __tablename__ = 'Product_Variation'
    id = Column(String, primary_key=True)
    id_product = Column(String, ForeignKey('Product.id'), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    cost = Column(BigInteger, nullable=False)

    products = relationship("Product", back_populates="products_variations")
    purchased_variations = relationship("Purchased_Variation", back_populates="products_variations")