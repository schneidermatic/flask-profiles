from flask import Flask
from flask import render_template, request

app = Flask(__name__, template_folder="views")

@app.route('/')
def read_index():
    name = request.args.get('name')
    number = request.args.get('number')
    return render_template('index.html', name=name, number=number)


if __name__ == '__main__':
   app.run()
