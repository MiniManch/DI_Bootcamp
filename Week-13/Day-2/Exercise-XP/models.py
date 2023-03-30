from __init__ import db 

class user(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(50), nullable=False)
    street   = db.Column(db.String(50),nullable=False)
    city     = db.Column(db.String(50),nullable=False)
    zipcode  = db.Column(db.String(50),nullable=False)

print('hello')