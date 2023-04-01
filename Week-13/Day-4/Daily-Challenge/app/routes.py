from flask import render_template, url_for, request, redirect, flash
from app import app, db
from app import models

prefix = '+972'


@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html', people=models.Person.query.all())


@app.route('/person_by_number/<int:number>')
def get_person_by_number(number):
	phone = models.PhoneNumber.query.filter_by(number=number).first().owner
	return render_template('get_person.html', prefix=prefix, person=models.Person.query.filter_by(id=phone).first())


@app.route('/person_by_name/<string:name>')
def get_person_by_name(name):
	people = []
	for person in models.Person.query.all():
		people.append(person.name)

	if name not in people:
		return render_template('404.html'), 404
	return render_template('get_person.html', prefix=prefix, person=db.session.query(models.Person).filter_by(name=name).first())


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')