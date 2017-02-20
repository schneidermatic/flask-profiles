import datetime, re

from app import db

class Tag(db.Model):
   id   = db.Column(db.Integer, primary_key=True)
   name = db.column(db.String(64))
   slug = db.Column(db.String(64), unique=True)

   def __init__(self, *args, **kwargs):
       super(Tag, self).__init__(*args, **kwargs)
       self.slug = slugify(self.name)

   def __repr__(self):
       return '<Tag: %s>' % self.slug
