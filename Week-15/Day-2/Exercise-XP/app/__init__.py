import flask
from flask_sqlalchemy import SQLAlchemy
import flask_migrate


flask_app = flask.Flask(__name__)

# Secret Key
flask_app.config['SECRET_KEY'] ='this is a secret shhh'
flask_app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:admatainov14!@localhost/exercises?charset=utf8mb4'

# configuring the database
db = SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

# connection blueprints
from app.films_bp import films_bp
from app.accounts_bp import accounts_bp

flask_app.register_blueprint(films_bp, url_prefix="/films")
flask_app.register_blueprint(accounts_bp, url_prefix="/accounts")

with flask_app.app_context():
	db.drop_all()
	db.create_all()