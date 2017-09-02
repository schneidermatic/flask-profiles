
import os, sys

sys.path.append(os.getcwd())

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bootstrap import db
from models import *

if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432')
    conn = engine.connect()
    try:
       conn.execute("commit")
       conn.execute("drop database pyswagger_db")
    except Exception as other:
       print("Can't delete 'pyswagger_db' because of:", other)

    try:
       conn.execute("commit")
       conn.execute("create database pyswagger_db")
    except Exception as other:
       print("Can't create 'pyswagger_db' because of:", other)

    conn.close()

    from flask_sqlalchemy import SQLAlchemy

    db.create_all()
    persons = [Identity(firstname='Max', lastname='Payne')]
    db.session.add_all(persons)
    db.session.commit()

    db.session.close()
