from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object("application.config.Config")
mongo = PyMongo(app)

from application import routes
