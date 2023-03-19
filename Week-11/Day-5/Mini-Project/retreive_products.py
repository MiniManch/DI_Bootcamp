import json 
data = []
with open('static/image_links.txt','r+') as f:
	image_list = [x for x in f.readlines()]
	with open('static/products.json','r+') as json_file:
		for line in json_file.readlines():
			objects = json.loads(line)
		for obj in objects: 
			new_obj = obj
			new_obj['Image'] = image_list.pop(0)
			data.append(new_obj)


def get_product_by_id(list_of_objs,product_id):
	for obj in list_of_objs:
		if obj['ProductId'] == product_id:
			return obj
	return False

def get_list_of_dict_atr(some_dict,atr):
	my_list = []
	for item in some_dict:
		my_list.append(item[atr])
	return list(set(my_list))

categories = get_list_of_dict_atr(data,'Category')