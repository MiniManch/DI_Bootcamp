from flask import Flask , render_template, url_for,request
from forms import add_user
from __init__ import user,app,db

@app.route('/')
@app.route('/home')
def home():
  return render_template('index.html',users = user )


@app.route('/add_user',methods=['GET','POST'])
def add_user_route():
  myForm = add_user()
  if myForm.is_submitted():
      this_user = user(id = request.form.get('id'),
                            name = request.form.get('name'),
                            street =  request.form.get('street'),
                            city = request.form.get('city'),
                            zipcode = request.form.get('zipcode')
                            )
      db.session.add(this_user)  
      db.session.commit()
      return redirect(url_for('home'))    
  return render_template('AddUser.html',form = myForm)