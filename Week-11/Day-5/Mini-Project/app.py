from flask import Flask,render_template,redirect
import flask
from retreive_products import data,get_product_by_id,categories

app = Flask(__name__)
app.config["DEBUG"] = True

# uploaded all the images 

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html',categories1 = categories[0:5],categories2 = categories[5:10])


# A products page, that displays a list of all the products that are for sale, routed to /products.
@app.route('/products')
def products():
	return render_template('products.html',products = data)

@app.route('/product_details/<product_id>')
def product_details(product_id):
	return render_template('product_details.html',product = get_product_by_id(data,product_id))

cart_items = []
@app.route('/cart')
def cart():
	total = 0
	for item in cart_items:
		total += item['Price']
	return render_template('cart.html',items = cart_items,total=total)

@app.route('/add_to_cart/<product_id>')
def add_to_cart(product_id):
	cart_items.append(get_product_by_id(data,product_id))
	return redirect(flask.url_for('products'))

@app.route('/cart_remove_item/<product_id>')
def remove_from_cart(product_id):
	cart_items.remove(get_product_by_id(data,product_id))
	return redirect(flask.url_for('cart'))


if __name__ == "__main__":
	app.run() 