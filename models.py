#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from run import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

# Need to put following 3 config statements above the db instantiation in db = SQLAlchemy(app)
app.config['DEBUG'] = True # For the server then will reload itself with any changes in code
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ytsnozrropwoym:611808c63f96c74d7b755cebc8857cabac5b94215097046256d8cd6855323254@ec2-174-129-236-147.compute-1.amazonaws.com:5432/d7qvs0a0ed4uf'
db = SQLAlchemy(app)
engine = create_engine('postgres://ytsnozrropwoym:611808c63f96c74d7b755cebc8857cabac5b94215097046256d8cd6855323254@ec2-174-129-236-147.compute-1.amazonaws.com:5432/d7qvs0a0ed4uf')

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer(), primary_key=True)

    title = db.Column(db.String(80), unique=True)
    post_text = db.Column(db.String(255))

    def __init__(self, id, title, post_text):
        self.id = id
        self.title = title
        self.post_text = post_text

class official_reviews(db.Model):
    __tablename__ = 'official_reviews'

    review_id = db.Column(db.String(100), primary_key=True)
    student_token = db.Column(db.String(80))
    m1 = db.Column(db.Integer())
    m2 = db.Column(db.Integer())
    m3 = db.Column(db.Integer())
    m4c = db.Column(db.Integer())
    m5c = db.Column(db.Integer())
    mod_class_id = db.Column(db.String(80))
    mod_class_name = db.Column(db.String(255))
    mod_term = db.Column(db.Integer())
    mod_ay = db.Column(db.Integer())
    mod_sem = db.Column(db.Integer())
    mod_rptterm = db.Column(db.Integer())
    mod_module_code = db.Column(db.Integer())

    def __init__(self, review_id, student_token, m1, m2, m3, m4c, m5c, mod_class_id, mod_class_name, mod_term, mod_ay, mod_sem ,mod_rptterm, mod_module_code):
        
        self.review_id = review_id
        self.student_token = student_token
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4c = m4c
        self.m5c = m5c
        self.mod_class_id = mod_class_id
        self.mod_class_name = mod_class_name
        self.mod_term = mod_term
        self.mod_ay = mod_ay
        self.mod_sem = mod_sem
        self.mod_rptterm = mod_rptterm
        self.mod_module_code = mod_module_code
