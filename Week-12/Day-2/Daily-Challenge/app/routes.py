from __main__ import app
import flask 
from forms import MyForm

@app.route('/',methods=['GET','POST'])
def home():
	name = None
	cvform = MyForm()
	if cvform.validate_on_submit():
		name = cvform.name.data
		cvform.name.data = ''

	return flask.render_template('index.html',  form = cvform,user_class = 'white' )

print('routes')