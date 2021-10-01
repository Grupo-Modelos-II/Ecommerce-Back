from datetime import datetime

from uuid import uuid4

from config.databaseConfig import Base

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, BigInteger, Date

class Transaction(Base):
    __tablename__ = 'Transaction'
    id = Column(String, primary_key=True)
    id_client = Column(String, ForeignKey('Client.id'), nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.now)
    total = Column(BigInteger, nullable=False)

    clients = relationship('Client', back_populates='transactions')
    purchases = relationship('Purchased', back_populates='transactions')

    def __init__(self,**kwargs):
       self.id = str(uuid4())
       self.id_client = kwargs['id_client']
       self.date = kwargs['date']
       self.total = kwargs['total']
      

    def to_dict(self):
       return {
            'id':self.id,
            'id_client':self.id_client,
            'date':self.date,
            'total':self.total,
            'clients':self.clients,
            'purchases':self.purchases
        }

class Purchased(Base):
    __tablename__ = 'Purchased'
    id = Column(String, primary_key=True)
    id_transaction = Column(String, ForeignKey('Transaction.id'), nullable=False)
    id_product = Column(String, ForeignKey('Product.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    cost = Column(BigInteger, nullable=False)

    transactions = relationship('Transaction', back_populates='purchases')
    purchased_variations = relationship('Purchased_Variation', back_populates='purchases')

    def __init__(self,**kwargs):
        self.id = str(uuid4())
        self.id_transaction = kwargs['id_transaction']
        self.id_product = kwargs['id_product']
        self.amount = kwargs['amount']
        self.cost = kwargs['cost']

    def to_dict(self):
        return {
            'id':self.id,
            'id_transaction':self.id_transaction,
            'id_product':self.id_product,
            'amount':self.amount,
            'cost':self.cost
        }

class Purchased_Variation(Base):
    __tablename__ = 'Purchased_Variation'
    id_purchased = Column(String, ForeignKey('Purchased.id'), primary_key=True)
    id_variation = Column(String, ForeignKey('Product_Variation.id'), primary_key=True)

    purchases = relationship('Purchased', back_populates='purchased_variations')
    products_variations = relationship('Product_Variation', back_populates='purchased_variations')

    def __init__(self,**kwargs):
        self.id_purchased = kwargs['id_variation']
        self.id_variation = kwargs['id_variation']

    def to_dict(self):
        return {
            'id_purchased':self.id_purchased,
            'id_variation':self.id_variation,
            'purchases':self.purchases,
            'products_variations':self.products_variations
        }