#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Not being used now, only using if app.py gets too big and I needa separate into components

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# coding: utf-8
from sqlalchemy import BigInteger, Column, Float, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class KaggleMarketingDsc3214(Base):
    #__abstract__ = True
    __tablename__ = 'kaggle_marketing_dsc3214'

    index = db.Column(db.BigInteger, primary_key=True, index=True)
    ad_id = Column(BigInteger)
    xyz_campaign_id = Column(BigInteger)
    fb_campaign_id = Column(BigInteger)
    age = Column(Text)
    gender = Column(Text)
    interest = Column(BigInteger)
    Impressions = Column(BigInteger)
    Clicks = Column(BigInteger)
    Spent = Column(Float(53))
    Total_Conversion = Column(BigInteger)
    Approved_Conversion = Column(BigInteger)

def __repr__(self):
        return self.name

def __init__(self, data):
    """
    Class constructor
    """
    self.index = data.get('index')
    self.ad_id = data.get('ad_id')
    self.xyz_campaign_id = data.get('xyz_campaign_id')
    self.fb_campaign_id = data.get('fb_campaign_id')
    self.age = data.get('age')
    self.gender = data.get('gender')
    self.interest = data.get('interest')
    self.Impressions = data.get('Impressions')
    self.Clicks = data.get('Clicks')
    self.Spent = data.get('Spent')
    self.Total_Conversion = data.get('Total_Conversion')
    self.Approved_Conversion = data.get('Approved_Conversion')

def save(self):
    db.session.add(self)
    db.session.commit()

def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

def delete(self):
    db.session.delete(self)
    db.session.commit()

@staticmethod
def get_all_users():
    return UserModel.query.all()

@staticmethod
def get_one_user(id):
    return UserModel.query.get(id)

  
def __repr(self):
    return '<id {}>'.format(self.id)
