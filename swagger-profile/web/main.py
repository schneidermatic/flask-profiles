from bootstrap import app, db, Swagger, jsonify
from models import Identity
import flask_restless

@app.route('/authors/<identity>/')
def authors(identity):
    """Example endpoint return a list of authors by identity
    This is using docstring for specifications
    ---
    tags:
      - authors
    parameters:
      - name: identity
        in: path
        type: string
        enum: ['all', 'rgb', 'cmyk']
        required: true
        default: all
        description: Which identity to filter?
    operationId: get_authors
    consumes:
      - application/json
    produces:
      - application/json
    security:
      authors_auth:
        - 'write:authors'
        - 'read:authors'
    schemes: ['http', 'https']
    deprecated: false
    externalDocs:
      description: Project repository
      url: http://github.com/rochacbruno/flasgger
    definitions:
      identity:
        type: object
        properties:
          identity_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of authors (may be filtered by identity)
        schema:
          $ref: '#/definitions/identity'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    author = Identity.query.filter_by(firstname='Max').first()
    all_authors = {
        'cmyk': [author.firstname, author.lastname],
        'rgb': ['red', 'green', 'blue']
    }
    if identity == 'all':
        result = all_authors
    else:
        result = {identity: all_authors.get(identity)}

    return jsonify(result)


if __name__ == '__main__':
    manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
    manager.create_api(Identity, url_prefix='/authors', methods=['GET', 'POST', 'DELETE'])

    app.run(debug=True, host='0.0.0.0', port=5000)
