from bootstrap import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    
    def __init__(self, *args, **kwargs):
       super(Author, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Author %r>' % self.firstname
