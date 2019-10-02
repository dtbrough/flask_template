
from my_app import db


class Table1(db.Model):
    column1 = db.Column(db.Integer, primary_key=True)
    column2 = db.Column(db.String(100))
    column3 = db.Column(db.String(50))
    column4 = db.Column(db.Integer)


class Table2(db.Model):
    column1 = db.Column(db.Integer, primary_key=True)
    column2 = db.Column(db.String(100))
    column3 = db.Column(db.String(50))
    column4 = db.Column(db.Integer)
