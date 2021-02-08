from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

def create_app():
    app = Flask(__name__)
    app.config.from_object('config') 
    return app

app=create_app()
db = SQLAlchemy(app)
import app