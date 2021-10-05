from datetime import datetime

from uuid import uuid4

from config.databaseConfig import Base

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger

class Transaction(Base):
    __tablename__ = 'Transaction'
    id = Column(String, primary_key=True)
    id_client = Column(String, ForeignKey('Client.id'), nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.now)
    total = Column(BigInteger, nullable=False)

    client = relationship('Client', back_populates='transactions')
    purchases = relationship('Purchased', back_populates='transaction')

    def __init__(self,**kwargs):
       self.id = str(uuid4())
       self.id_client = kwargs['id_client']
       self.total = kwargs['total']
      

    def to_dict(self):
       return {
            'id':self.id,
            'id_client':self.id_client,
            'date':self.date,
            'total':self.total,
            'client':self.client,
            'purchases':self.purchases
        }
    
    def update(self, **kwargs):
        self.id = kwargs['id'] or self.id
        self.id_client = kwargs['id_client'] or self.id_client
        self.total = kwargs['total'] or self.total

class Purchased(Base):
    __tablename__ = 'Purchased'
    id = Column(String, primary_key=True)
    id_transaction = Column(String, ForeignKey('Transaction.id'), nullable=False)
    id_product = Column(String, ForeignKey('Product.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    cost = Column(BigInteger, nullable=False)

    transaction = relationship('Transaction', back_populates='purchases')
    product = relationship('Product', back_populates='purchases')

    def __init__(self,**kwargs):
        self.id = str(uuid4())
        self.id_transaction = kwargs['id_transaction']
        self.id_product = kwargs['id_product']
        self.amount = kwargs['amount']
        self.cost = kwargs['cost']

    def to_dict(self):
        return {
            'id':self.id,
            'transaction':self.transaction,
            'product':self.product,
            'amount':self.amount,
            'cost':self.cost
        }
