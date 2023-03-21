from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Bulbasaur'
app.config['DEBUG']      = True
import routes

if __name__ == '__main__':
	app.run()