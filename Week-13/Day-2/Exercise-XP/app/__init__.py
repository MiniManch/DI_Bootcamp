from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_migrate
from app.my_functions import get_random_string,populate_database
app = Flask(__name__)

# configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:admatainov14!@localhost/users?charset=utf8mb4' 

# Secret Key
app.config['SECRET_KEY'] = get_random_string(256)
# app.config['DEBUG'] = True

# Initialize The Database 
db = SQLAlchemy(app)

from app import routes,models

migrate = flask_migrate.Migrate(app,db)

my_file = 'app/static/users.json'

with app.app_context():
	# will delete all users, drop table, create table, then repopulate table.
	db.drop_all()
	db.create_all()
	populate_database(db,models.User,my_file)