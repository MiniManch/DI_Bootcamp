from app import db

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(50), nullable=False)
    street   = db.Column(db.String(50),nullable=False)
    city     = db.Column(db.String(50),nullable=False)
    zipcode  = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}, street :{self.street}, city: {self.city}, zipcode: {self.zipcode}'