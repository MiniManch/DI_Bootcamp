import flask
from flask_sqlalchemy import SQLAlchemy
import flask_migrate
from flask_login import LoginManager
import os

flask_app = flask.Flask(__name__)

# Secret Key
flask_app.config['SECRET_KEY'] = f'{os.environ["SECRET_KEY"]}'
flask_app.config['SQLALCHEMY_DATABASE_URI'] =f'mysql+pymysql://{os.environ["MYSQL_USER"]}:{os.environ["MYSQL_PASSWORD"]}@{os.environ["MYSQL_DATABASE_NAME"]}?charset=utf8mb4'

# configuring the database
db = SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

# Flask Login
login_manager = LoginManager()
login_manager.login_view = 'accounts_bp.login'
login_manager.init_app(flask_app)

from app.accounts_bp.models import User


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


# connection blueprints
from app.films_bp import films_bp
from app.accounts_bp import accounts_bp


flask_app.register_blueprint(films_bp, url_prefix="/films")
flask_app.register_blueprint(accounts_bp, url_prefix="/accounts")


with flask_app.app_context():
	db.drop_all()
	db.create_all()