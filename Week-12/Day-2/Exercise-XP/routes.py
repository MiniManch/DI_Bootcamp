from flask import Flask , render_template, url_for,request
from __main__ import app
from forms import add_city
import json

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/add_a_city',methods=['GET','POST'])
def add_a_city():
	myForm = add_city()
	if myForm.is_submitted():
		with open('static/cities.json','a') as json_file:
			json_file.write(',') #so we can iterate over the file and seperate lines by ,
			json_file.write(json.dumps(request.form.to_dict()))

	return render_template('add_a_city.html',form = myForm)


