
import os, sys

sys.path.append(os.getcwd())

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bootstrap import db
from models import Author


if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432') 
    conn = engine.connect()
    try:
       conn.execute("commit")
       conn.execute("drop database flask_rest")
    except Exception as other:
       print("Can't delete 'flask_rest' because of:", other)
    
    try:
       conn.execute("commit")
       conn.execute("create database flask_rest")
    except Exception as other:
       print("Can't create 'flask_rest' because of:", other)

    conn.close()
    
    from flask_sqlalchemy import SQLAlchemy
    
    
    db.create_all()
    authors = [
               Author(firstname='Max', lastname='Ramalho')
    ]
    db.session.add_all(authors)
    db.session.commit()
    
    db.session.close()
