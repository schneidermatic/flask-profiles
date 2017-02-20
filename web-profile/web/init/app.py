from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from conf.config import Configuration
import jinja2


app = Flask(__name__)

jinja_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader(['views']),
])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(Configuration)
app.jinja_loader = jinja_loader
db = SQLAlchemy(app)