from flask import Flask
from Config import Config

app = Flask(__name__)
app.config.from_object(Config)

from form import routes
