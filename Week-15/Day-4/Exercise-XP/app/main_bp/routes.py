import flask
from app.main_bp import main_bp
from flask_login import current_user,login_required
from app import db


@main_bp.route("/")
@main_bp.route("/homepage")
def index():
	return flask.render_template('index.html')

