from flask import render_template, request
from app import app

@app.route('/')
def index():
    name = request.args.get('name')
    number = request.args.get('number')
    return render_template('index.html', name=name, number=number)
