from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config.from_object('youtube_portal.config') 

db = SQLAlchemy(app)

import youtube_portal.app