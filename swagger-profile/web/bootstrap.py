from flask import Flask, jsonify
from flasgger import Swagger
import flask_sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/pyswagger_db'
app.config['SWAGGER'] = {
     'title': 'Authors API',
     'uiversion': 2
}
Swagger(app)
db = flask_sqlalchemy.SQLAlchemy(app)
