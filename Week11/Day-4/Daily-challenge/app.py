from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/color/<user_class>')
def color(user_class):
	return render_template('home.html',user_class=user_class)

if __name__ == "__main__":
	app.run()