import flask

from app.accounts_bp import accounts_bp


@accounts_bp.route("/login")
def login():
    name = 'emmanuel'
    return flask.render_template("login.html",name = name)
