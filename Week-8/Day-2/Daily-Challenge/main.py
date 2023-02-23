import typing

class Farm:
  def __init__(self,name,animals):
    self.name = name
    self.animals = animals
      
  def add_animal(self,name:str,num:int = 1): # you can make this function in just a single line: self.animals[name] = self.animals.get(name, 0) + num
    if name in self.animals.keys():
        self.animals[name] += num  
    else:
      self.animals[name] = num

  def get_info(self):
    print(f'{self.name}\'s farm \n')
    for animal in self.animals:
      if animal == list(self.animals.keys())[-1]:
        print(f'{animal} : {self.animals[animal]} \n')
      else:
        print(f'{animal} : {self.animals[animal]} ')
    print('    E-I-E-I-O') # you can use \t rather than the spaces

  def get_animal_types(self):
    animal_types = sorted(list(self.animals.keys()))
    return animal_types

  def get_short_info(self):
    string  = ''
    animals_list = self.get_animal_types()
    for animal in animals_list:
      if string == '':
        string = string + animal
      elif animal == animals_list[-1]:
        string = string + ", "+ 'and' + ' ' + animal
      else: 
        string =  string + ', ' + animal
    print(f'{self.name}\'s farm has {string}')


animals = {'sheep' : 1, 'dogs' : 5}
macdonald = Farm('McDonald',animals)

macdonald.add_animal('ducks',42)

macdonald.get_info()
macdonald.get_short_info()
