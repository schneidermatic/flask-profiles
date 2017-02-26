from flask import Flask
from flask import render_template, request
from views.blueprint import entries

app = Flask(__name__, template_folder="views")
app.register_blueprint(entries, url_prefix='/entries')

@app.route('/')
def read_index():
    name = request.args.get('name')
    number = request.args.get('number')
    return render_template('index.html', name=name, number=number)


if __name__ == '__main__':
   app.run()
