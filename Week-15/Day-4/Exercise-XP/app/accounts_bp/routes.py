import flask
from app.accounts_bp import accounts_bp
from app import db
from .forms import User_Form
from app.accounts_bp import models
from flask_login import login_user, login_required, logout_user,current_user
from werkzeug.security import generate_password_hash,check_password_hash


@accounts_bp.route("/signup", methods=['GET', 'POST'])
def signup():
    form = User_Form()
    print(f'before:{current_user.is_authenticated}')
    if form.validate_on_submit():
        if models.User.query.filter_by(email=form.email.data).first() is None:
            new_user = models.User(email=form.email.data, password=generate_password_hash(form.password.data, method='sha256'), username=form.username.data)
            db.session.add(new_user)
            db.session.commit()
            flask.flash(f'new user {form.username.data} is created!')
            print(f'after:{current_user.is_authenticated}')
            return flask.redirect(flask.url_for('films_bp.index'))

        flask.flash('User already exists, try again')
        return flask.redirect(flask.url_for('accounts_bp.signup'))
    return flask.render_template("signup.html", form=form, title='Sign up')


@accounts_bp.route("/login", methods=['GET', 'POST'])
def login():
    print(current_user.username)
    form = User_Form()
    if flask.request.method == 'POST':
        user =  models.User.query.filter_by(email=form.email.data).first()
        if user is None:
            flask.flash('Email does not exist , try again')
            return flask.redirect(flask.url_for('accounts_bp.login'))
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flask.flash(f'Welcome {current_user.username}')
                return flask.redirect(flask.url_for('films_bp.index'))

            else:
                flask.flash('Wrong password, try again')
                return flask.redirect(flask.url_for('accounts_bp.login'))
    return flask.render_template("login.html", form=form, title='Login')

