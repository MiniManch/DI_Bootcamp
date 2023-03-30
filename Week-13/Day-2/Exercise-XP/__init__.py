from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
import flask_migrate
import random 
from my_functions import get_random_string,populate_database
from forms import add_user

app = Flask(__name__)

# configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:admatainov14!@localhost/users?charset=utf8mb4' 

# Secret Key
app.config['SECRET_KEY'] = get_random_string(256)
app.config['DEBUG'] = True

# Initialize The Database 
db = SQLAlchemy(app)

# initialize the migrate object
migrate = flask_migrate.Migrate(app,db)

# Defining model
class user(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(50), nullable=False)
    street   = db.Column(db.String(50),nullable=False)
    city     = db.Column(db.String(50),nullable=False)
    zipcode  = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}, street :{self.street}, city: {self.city}, zipcode: {self.zipcode}'

my_file = 'static/users.json'

with app.app_context():
    for each_user in user.query.all():
        db.session.delete(each_user)
    # for each_user in user.query.all():
    #     print(each_user)
    db.session.commit()
    db.drop_all()
    # create db and populate
    db.create_all()
    populate_database(db,user,my_file)

    # routes
    import routes
    # @app.route('/')
    # @app.route('/home')
    # def home():
    #     return render_template('index.html',users = user )


    # @app.route('/add_user',methods=['GET','POST'])
    # def add_user_route():
    #     myForm = add_user()
    #     if myForm.is_submitted():
    #         this_user = user(id = request.form.get('id'),
    #                               name = request.form.get('name'),
    #                               street =  request.form.get('street'),
    #                               city = request.form.get('city'),
    #                               zipcode = request.form.get('zipcode')
    #                               )
    #         db.session.add(this_user)  
    #         db.session.commit()
    #         return redirect(url_for('home'))    
    #     return render_template('AddUser.html',form = myForm)


    if __name__ == "__main__":
        app.run() 
    print('yello')
