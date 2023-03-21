class pagination_class():
	def __init__(self,collection,num_of_pages):
		self.collection         = collection
		self.pages              = num_of_pages
		self.items_on_last_page = self.num_of_items() % self.pages
		self.items_per_page     = int(((self.num_of_items() - self.items_on_last_page) / self.pages))
		self.paginated          = self.paginate()

	def num_of_items(self):
		return len(self.collection)

	def calc_items_per_page(self):
		return {'per_page': self.items_per_page,'last_page':self.items_on_last_page,'pages':self.pages}

	def paginate(self):
		copy_collection = self.collection.copy()
		new_collection  = {}
		for i in range(0,self.pages+1):
			if len(copy_collection) < self.items_per_page:
				new_collection[f'{i}'] = copy_collection[:]
				break
			chunk  = copy_collection[0:self.items_per_page]
			new_collection[f'{i}'] = chunk
			for i in range(0,self.items_per_page):
				copy_collection.pop(0)
		return new_collection

