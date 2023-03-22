from flask import Flask,render_template,url_for
import random 
from random_string import get_random_string

app = Flask(__name__)

# Part I: Secret Key
app.config['SECRET_KEY'] = get_random_string(256)
app.config['DEBUG'] = True


# Part II: Create The Form
from forms import add_city
import routes

# To get all list of lines from json 
# with open('static/cities.json','r') as file:
# 		lines = file.read().split(',')
# 		for line in lines:
# 			if line == '':
# 				lines.remove(line)
# 		print(lines)

if __name__ == '__main__':
	app.run()