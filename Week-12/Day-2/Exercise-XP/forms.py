import flask 
from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField,SubmitField)
from wtforms.validators import InputRequired, Length

class add_city(FlaskForm):
	name                  = StringField('What is its name? ', validators=[InputRequired()])
	area                  = IntegerField('Area (in square km)',validators = [InputRequired()])
	num_of_inhabitants    = IntegerField('Number of Inhabitants',validators = [InputRequired()])
	country               = StringField('Country',validators = [InputRequired()])
	submit                = SubmitField('Submit') 

    

   