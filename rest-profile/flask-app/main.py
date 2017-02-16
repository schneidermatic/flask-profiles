from bootstrap import app, db
from models import Author
import flask_restless

if __name__ == '__main__':
    manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
    manager.create_api(Author, url_prefix='/api/v1', methods=['GET', 'POST', 'DELETE'])
     
    app.run(debug=True, host='0.0.0.0', port=5000)
