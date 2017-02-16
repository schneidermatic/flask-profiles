from flask import render_template, request
from init.app import app,db

@app.route('/')
def index():
    name = request.args.get('name')
    number = request.args.get('number')
    return render_template('index.html', name=name, number=number)