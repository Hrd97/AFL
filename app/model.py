# -*- coding: utf-8 -*-
from . import db
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.CHAR(50),unique=True)
    email = db.Column(db.CHAR(50))
    password = db.Column(db.VARCHAR(100))
    desc = db.Column(db.VARCHAR(500))

class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    uploadtime=db.Column(db.DATE)
    name = db.Column(db.VARCHAR(100),unique=True)
    status = db.Column(db.VARCHAR(100))
    visibility = db.Column(db.CHAR(1))
    path = db.Column(db.VARCHAR(300))
    description = db.Column(db.VARCHAR(1000))
    star = db.Column(db.Integer)
    comment = db.Column(db.Integer)
    user = db.relationship('User', backref=db.backref('project'))


class Collect(db.Model):
    __tablename__ = 'collect'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    projectid = db.Column(db.Integer, db.ForeignKey('project.id'))
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    project = db.relationship('Project', backref=db.backref('collect'))


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    projectid = db.Column(db.Integer, db.ForeignKey('project.id'))
    username = db.Column(db.CHAR(50))
    commenttime=db.Column(db.DATE)
    time = db.Column(db.CHAR(50))
    repliedname = db.Column(db.CHAR(50))
    content=db.Column(db.VARCHAR(300))
    star=db.Column(db.Integer)



class Like(db.Model):
    __tablename__ = 'like'
    commentid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, primary_key=True)
    projectid=db.Column(db.Integer, primary_key=True)

