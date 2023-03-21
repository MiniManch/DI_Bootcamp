from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FloatField,TextAreaField,EmailField
from wtforms.validators import DataRequired,NumberRange

class MyForm(FlaskForm):
    name   = StringField('Whats Your Name? ', validators=[DataRequired()])
    age    = FloatField('age',validators = [DataRequired()])
    experience = TextAreaField('Work Experience')
    email      = EmailField('Email',validators = [DataRequired()])
    submit = SubmitField('Submit') 

   