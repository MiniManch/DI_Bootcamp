from app import db
import datetime


class Country(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	films_from = db.relationship('Film', backref='countries')


# secondary tables
film_available_in_table = db.Table(
	'available_in',
	db.Column('film_id', db.Integer, db.ForeignKey('film.id')),
	db.Column('country_id', db.Integer, db.ForeignKey('country.id'))
)

categories_for_films = db.Table(
	'film_categories',
	db.Column('film_id', db.Integer, db.ForeignKey('film.id')),
	db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
)

film_directors = db.Table(
	'film_directors',
	db.Column('film_id', db.Integer, db.ForeignKey('film.id')),
	db.Column('director_id', db.Integer, db.ForeignKey('director.id'))
)


class Category(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(100), nullable=False, primary_key=True)


class Film(db.Model):
	id = db.Column(db.Integer, autoincrement=True, primary_key=True )
	title = db.Column(db.String(100), nullable=False,primary_key=True)
	release_date = db.Column(db.Date, default=datetime.date.today())
	created_in_country = db.Column(db.Integer, db.ForeignKey('country.id'))
	available_in_countries = db.relationship('Country', secondary=film_available_in_table, backref=db.backref('films_avail_in',uselist=True))
	categories = db.relationship('Category', secondary=categories_for_films, backref=db.backref('films',uselist=True))
	director = db.relationship('Director', secondary=film_directors, backref=db.backref('director_films',uselist=True))


class Director(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	first_name = db.Column(db.String(100), nullable=False)
	last_name = db.Column(db.String(100), nullable=False)


