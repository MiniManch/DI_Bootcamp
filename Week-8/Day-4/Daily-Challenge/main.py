# Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# The Pagination class will accept 2 parameters:

# items (default: []): A list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.
# So for example we could initialize our pagination like this:


class Pagination:

  def __init__(self, string='', pageSize=10):
    self.string = string
    self.pageSize = pageSize
    self.page_list = []

# getVisibleItems() : returns a list of items visible depending on the pageSize

  def getVisibleItems(self):
    try:
      self.visItem
    except:
      print('except')
      copy_list = (self.string + '.')[:-1]
      for index, item in enumerate(self.string):
        if index % self.pageSize == 0:
          part = copy_list[0:self.pageSize]
          self.page_list.append(part)
          copy_list = copy_list.replace(part, '')
          self.visItem = self.page_list[0]
    return self.visItem


# perhaps next page should only change the page we're on, and then we check what page were on and display that via get visibile, but again that dictates that we need to check if there is that. r

  def nextPage(self):
    if not self.visItem:
      visItem = self.getVisibleItems()
    else:
      visItem = self.visItem
    index = self.page_list.index(visItem)
    if index + 1 < len(self.page_list):
      self.visItem = self.page_list[index + 1]
    else:
      self.visItem = self.page_list[-1]
    return self

  def prevPage(self):
    if not self.visItem:
      return self.getVisibleItems()
      print('this is the first page! cant go back')
    index = self.page_list.index(self.visItem)
    if index - 1 <= 0:
      self.visItem = self.page_list[0]
    else:
      self.visItem = self.page_list[index - 1]
    return self
    
  def firstPage(self):
    self.visItem = self.page_list[0]
    return self

  def lastPage(self):
    self.visItem = self.page_list[-1]
    return(self)
    
  def goToPage(self,num = 0):
    while num -1 > (len(self.page_list )-1) or num -1 < 0 :
      num = int(input(f'Please enter a number between 1 and  {len(self.page_list)} \n'))
    self.visItem = self.page_list[num- 1]
    return self


alphabetList = "abcdefghijklmnopqrstuvwxyz"
p = Pagination(alphabetList, 4)
print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())

p.goToPage(25)
print(p.getVisibleItems())
