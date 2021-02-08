from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



class Thread(db.Model):
    #__tablename__ = "threads"
    id = db.Column(db.Integer, primary_key=True)
    threadname = db.Column(db.String(80), unique=True)
    articles = db.relationship('Article', backref='thread', lazy=True)

    def __init__(self, threadname, articles=[]):
        self.threadname = threadname
        self.articles = articles

class Article(db.Model):
    #__tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_date = db.Column(db.DateTime, nullable=False,
                                default=datetime.utcnow())
    name = db.Column(db.String(80))
    article = db.Column(db.Text())
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)

    def __init__(self, pub_date, name, article, thread_id):
        self.pub_date = pub_date
        self.name = name
        self.article = article
        self.thread_id = thread_id