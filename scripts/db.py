from app import db
from datetime import datetime

#DATETIME_PATTERN = r"%d-%m-%Y %H:%M:%S"

class Document(db.Model):
    __searchable__ = ['text']
    id = db.Column(db.Integer, primary_key=True)
    rubrics = db.Column(db.String())
    text = db.Column(db.Text())
    created_date = db.Column(db.DateTime)
    

    def __init__(self, id, txt, date, rubrics):
        self.id = id
        self.rubrics = rubrics
        self.text = txt
        self.created_date = datetime.strptime(date, DATETIME_PATTERN)
