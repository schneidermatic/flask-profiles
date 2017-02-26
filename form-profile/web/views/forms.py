import wtforms

from models import Author

class EntryForm(wtforms.Form):
    firstname = wtforms.StringField('Firstname')
    lastname = wtforms.TextField('Lastname')
    
    def save_entry(self, entry):
        self.populate_obj(entry)
        return entry