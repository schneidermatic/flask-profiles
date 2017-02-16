import flask
import flask_sqlalchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/flask_rest'
db = flask_sqlalchemy.SQLAlchemy(app)
