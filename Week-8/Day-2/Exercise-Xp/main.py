# 🌟 Exercise 1: Cats
# Using this class
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Instantiate three Cat objects using the code provided above.
cat_1 = Cat('Picasso',94)
cat_2 = Cat('Molly',4)
cat_3 = Cat('Kodak',12)

# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
list_of_cats = [cat_1,cat_2,cat_3]
def oldest_cat(list_of_items):
  oldest = 0
  oldest_id = ''
  for index,item in enumerate(list_of_items):
    if item.age > oldest:
      oldest    = item.age
      oldest_id = index 
    # print(item.age)
  return oldest_id,oldest

oldest = oldest_cat(list_of_cats)
oldest_cat_name = list_of_cats[oldest[0]].name
oldest_cat_age  = oldest[1]
print(f' the oldest cat is {oldest_cat_name}, and is {oldest_cat_age} years old')


# 🌟 Exercise 2 : Dogs
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height.
# This function instantiates two attributes, which values are the parameters.
class Dog:
  def __init__(self,name,height):
    self.name   = name
    self.height = height
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
  def bark(self):
    string = f'{self.name} goes woof!'
    return string
  # Create a method called jump that prints the following string:
  # “<dog_name> jumps <x> cm high!”. x is the height*2.
  def jump(self):
    string = f'{self.name} jumps {self.height*2}cm high!'
    return string

# Outside of the class, create an object called davids_dog.
# His dog’s name is “Rex” and his height is 50cm.
davids_dog = Dog('Rex',50)

# Print the details of his dog (ie. name and height) and call the methods bark and jump.
print(davids_dog.name,davids_dog.height)
print(davids_dog.jump())
print(davids_dog.bark())

# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
sarahs_dog = Dog('Teacup',20)

# Print the details of her dog (ie. name and height) and call the methods bark and jump.
print(sarahs_dog.name,sarahs_dog.height)
print(sarahs_dog.jump())
print(sarahs_dog.bark())

bigger = 0
list_of_dogs = [sarahs_dog,davids_dog]

for index,dog in enumerate(list_of_dogs):
  if dog.height > bigger:
    bigger = dog.height
    bigger_dog = list_of_dogs[index]
print(f'The bigger dog is {bigger_dog.name} he is {bigger_dog.height}cm tall!!')


# 🌟 Exercise 3 : Who’s The Song Producer?
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
class Song:
  def __init__(self,lyrics: list):
    self.lyrics = lyrics
   # Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line. 
  def sing_me_a_song(self):
    for lyric in self.lyrics:
      print(lyric)


Heartless_lyrics = ["in the night I hear 'em talk","The coldest story ever told","Somewhere far along this road","He lost his soul to a woman so heartless","How could you be so heartless?"]
Heartless = Song(Heartless_lyrics)

# Then, call the sing_me_a_song method. The output should be:
Heartless.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
class Zoo:
  def __init__(self,zoo_name):
    self.name    = zoo_name
    self.animals = []
  # Create a method called add_animal that takes one parameter new_animal. 
  # This method adds the new_animal to the animals list as long as it isn’t already in the list.
  def new_animal(self,animal:str):
    if animal not in self.animals:
      self.animals.append(animal)
  # Create a method called get_animals that prints all the animals of the zoo.
  def get_animals(self):
    if len(self.animals) > 0:
      for animal in self.animals:
        print(animal)
    else:
      print(' We have no animals, its an empty zoo')
  # Create a method called sell_animal that takes one parameter animal_sold. 
  # This method removes the animal from the list and of course the animal needs to exist in the list.
  def sell_animal(self,animal:str):
    if animal in self.animals:
      self.animals.remove(animal)
      print(f'{animal} was sold!')
    else:
      print('We dont have that animal mister')
  # Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
  def sort_animals(self):
    animals_sorted= sorted(self.animals)
    animal_Dict  = {}
    i = 1
    for index,animal in enumerate(animals_sorted):
      first_letter_list = []
      if index+1 == len(animals_sorted):
        first_letter_list.append(animal)
        animal_Dict[i] = first_letter_list
        break
      else:
        first_letter = animal[0]
        for index,animal in enumerate(animals_sorted):
          if animal[0] == first_letter:
            first_letter_list.append(animal)
        if first_letter_list not in animal_Dict.values():
          animal_Dict[i] = first_letter_list
          i+=1
    return animal_Dict
  # Create a method called get_groups that prints the animal/animals inside each group.
  def get_groups(self):
    groups = list(self.sort_animals().values())
    print(groups)
    for index,group in enumerate(groups):
      i = index+1
      print(f'group {i} has : ')
      for animal in group:
        print(animal)
      
Ramat_gan = Zoo('Ramat-Gan')
Ramat_gan.new_animal('Iguana')
Ramat_gan.new_animal('Cougar')
Ramat_gan.new_animal('Cat')
Ramat_gan.new_animal('Bear')
Ramat_gan.new_animal('Baboon')
Ramat_gan.new_animal('Bat')

Ramat_gan.get_groups()
  