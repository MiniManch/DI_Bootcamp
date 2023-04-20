from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, SubmitField, PasswordField, DateField)
from wtforms.validators import InputRequired


class AddFilmForm(FlaskForm):
	title              = StringField('Title', validators=[InputRequired()], render_kw={"placeholder": 'Film Title'})
	release_Date       = DateField('Release Date', validators=[InputRequired()])
	country_created_in = StringField('Country Film was created in', validators=[InputRequired()])
	category           = StringField('Category', validators=[InputRequired()], render_kw={"placeholder": 'for instance "Action"'})
	submit       = SubmitField('Submit')


class AddDirectorForm(FlaskForm):
	first_name  = StringField('First Name', validators=[InputRequired()])
	last_name  = StringField('Last Name', validators=[InputRequired()])
	film       = StringField('Film')
	submit      = SubmitField('Submit')
