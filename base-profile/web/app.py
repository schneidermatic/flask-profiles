from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from conf.config import Configuration 

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(Configuration)
db = SQLAlchemy(app)