from app import db


class PhoneNumber(db.Model):
    id     = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    owner  = db.Column(db.Integer, db.ForeignKey("person.id"))

    def __init__(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)


class Person(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(50), nullable=False)
    email        = db.Column(db.String(120), nullable=False)
    address      = db.Column(db.String(200), nullable=False)
    phonenumbers = db.relationship("PhoneNumber", backref="phone_number", lazy="dynamic")

    def __init__(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)
