from flask import Flask,render_template
import json
import os
# Instructions :
# Instructions :
# Note: For this exercise, we will use the JSON file provided in the assets below.

# This database contains a list of dictionaries. Each dictionary contains these keys:

# ProductId, Category, MainCategory,TaxTarifCode, SupplierName, WeightMeasure
# WeightUnit, Description, Name, ProductPicUrl, Status, Quantity, UoM, CurrencyCode
# Price, Width, Depth, Height, DimUnit
# We will be using these keys to represent each item in our marketplace.
# You don’t have to use all the keys.

# Build a marketplace website, the website should have 3 pages:
# A homepage, with a welcome message, routed to /.
# A products page, that displays a list of all the products that are for sale, routed to /products.
# A product details page, that displays the details of the selected product 
# (the product id should be passed into the URL), routed to /product/<product_id>

app  = Flask(__name__)
# app.config["DEBUG"] = True - for debugging and just dev stuff

path = 'static/product_db.json' 
with open(path,'r+') as f:
	data =  json.loads(f.read())

def get_list_of_dict_atr(some_dict,atr):
	my_list = []
	for item in some_dict:
		my_list.append(item[atr])
	return list(set(my_list))

catergories = get_list_of_dict_atr(data,'Category')

# A homepage, with a welcome message, routed to /.
@app.route('/')
@app.route('/home')
def home():
	i = 0
	return render_template('home.html',categories1 = catergories[0:5],categories2 = catergories[5:10])

# A products page, that displays a list of all the products that are for sale, routed to /products.
@app.route('/products')
def products():
		return render_template('products.html',products = data[0:10])


@app.route('/product_details/<product_id>')
def product_details(product_id):
	for product in data:
		if product['ProductId'] == product_id:
			chosen_product = product

	return render_template('product_details.html',product = chosen_product)



if __name__ == "__main__":
	app.run()

