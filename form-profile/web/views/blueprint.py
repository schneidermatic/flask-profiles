from flask import Blueprint
from flask import render_template
from flask import request
from models import Author
from bootstrap import app
from bootstrap import db
from views.forms import EntryForm
from flask import redirect
from flask import url_for

entries = Blueprint('entries', __name__, template_folder='templates')

@entries.route('/')
def index():
    return "Hello"

@entries.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        form = EntryForm(request.form)
        if form.validate():
            entry = form.save_entry(Author())
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('entries.index'))
    
    form = EntryForm()
    return render_template('entries/create.html', form=form)