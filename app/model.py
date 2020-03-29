# -*- coding: utf-8 -*-
from . import db
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.CHAR(50))
    email = db.Column(db.CHAR(50))
    password = db.Column(db.VARCHAR(100))


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer)
    uploadtime=db.Column(db.DATE)
    name = db.Column(db.VARCHAR(100))
    status = db.Column(db.VARCHAR(100))
