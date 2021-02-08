import os

SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"  #os.environ.get('DATABASE_URL') or 
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY="secret key"