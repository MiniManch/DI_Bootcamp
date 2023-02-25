# Exercise XP+
# Create a class called Family and implement the following attributes:
# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
class Family:
  def __init__(self,members:list,last_name:str):
      self.members   = members
      self.last_name = last_name
  # born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
  def born(self,**kwargs):
    kwargs['age'] = 0
    kwargs['is_child'] = True
    self.members.append(kwargs)
    print('congrats on the new kid man have a good luck and stuff')
    return self.members
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
  def is_18(self,name:str):
    for member in self.members:
      if name == member['name']:
        member_index = self.members.index(member)
    if self.members[member_index]['age'] >=18:
      return True,member_index
    raise Exception('under 18')

  def family_presentation(self):
    print(self.last_name)
    for member in self.members:
      print(member['name'])
  
# Initial members data:
inital_list=[
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
  ]

# my_Family = Family(inital_list,'Beckham')

# print(my_Family.born(name='David',is_child='False',gender = 'Female'))

class TheIncredibles(Family):
  def use_power(self,member):
    try:
      is_18 = self.is_18(member)
      print(f"{member} can {self.members[is_18[1]]['power']}")
    except:
      print(f'{member} not over 18, he cant control his powers')

  def incredible_presentation(self):
    super().family_presentation()
    for member in self.members:
      print(member['incredible_name'])
      print(member['power'])
      
inc_mem = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'},
  {'name':'Domi','age':4,'gender':'male','is_child':False,'power': 'see through walls','incredible_name':'wall person'}
]


inc_fam = TheIncredibles(inc_mem,'Cohen')
inc_fam.born(name='Jack',power = 'unknown',incredible_name = 'baby jack',gender = 'Male')

inc_fam.incredible_presentation()
inc_fam.use_power('Sarah')
inc_fam.use_power('Domi')
