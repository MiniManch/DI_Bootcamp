from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_migrate
from app.my_functions import get_random_string, populate_database, redo_db, populate_number_database
from app import create_db

app = Flask(__name__)

# configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:admatainov14!@localhost/oneonefour?charset=utf8mb4'

# Secret Key
app.config['SECRET_KEY'] = get_random_string(256)
# app.config['DEBUG'] = True

# Initialize The Database 
db = SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from app import models
from app import routes

my_file = 'app/static/users.json'

with app.app_context():
	redo_db([models.Person, models.PhoneNumber], db)
	populate_database(db, models.Person)
	populate_number_database(db, models.PhoneNumber)
	db.session.commit()


