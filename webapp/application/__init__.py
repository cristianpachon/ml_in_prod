from flask import Flask

app = Flask(__name__)
app.config.from_object("application.config.Config")

from application import routes
