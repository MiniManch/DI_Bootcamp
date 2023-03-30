from flask import render_template, url_for, request, redirect,flash
from app.forms import add_user, login as login_form
from app import app, db
from app.models import User


@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html', users=User)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user_route():
	myForm = add_user()
	if myForm.is_submitted():
		this_user = User(id=request.form.get('id'),
		                 name=request.form.get('name'),
		                 street=request.form.get('street'),
		                 city=request.form.get('city'),
		                 zipcode=request.form.get('zipcode')
		                 )
		db.session.add(this_user)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('AddUser.html', form=myForm)


# Daily Challenge part
@app.route('/login', methods=['GET', 'POST'])
def login():
	myForm = login_form()
	if myForm.is_submitted():
		this_user = dict(request.form)
		users  = User.query.all()
		for user in users:
			print(user)
			if this_user['name'].isnumeric() or this_user['city'].isnumeric():
				flash(f'Please enter strings and not numbers', "error")
			if this_user['name']  == user.name and this_user['city'] == user.city:
				flash(f'You are now logged in {this_user["name"]}', "success")
				return redirect(url_for('home'))
		flash(f'You need to sign up!','user does not exist')
		return redirect(url_for('add_user_route'))
	return render_template('login.html', form=myForm)
