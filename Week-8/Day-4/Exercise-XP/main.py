import random
# Exercise XP
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Create another cat breed named Siamese which inherits from the Cat class.
class Siamese(Cat):
  def sing(self, sounds):
        return f'{sounds}'
# Create a list called all_cats, which holds three cat instances :
# one Bengal, one Chartreux and one Siamese.\
shlomi = Siamese('shlomi',4)
dan = Chartreux('dan',2)
mitzi = Bengal('mitzi',6)
# Those three cats are Sara’s pets.
# Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.

all_cats  = [shlomi,dan,mitzi]
sarah_pets = Pets(all_cats)

# Take all the cats for a walk, use the walk method.
sarah_pets.walk()

# 🌟 Exercise 2 : Dogs
# Create a class called Dog with the following attributes name, age, weight.
class Dog:
  def __init__(self,name,age,weight):
    self.name   = name
    self.age    = age
    self.weight = weight
# bark: returns a string which states: “<dog_name> is barking”.
  def bark(self):
    string = f'{self.name} is barking'
    return string
    
# run_speed: returns the dogs running speed (weight/age*10).
  def run_speed(self):
    speed = (self.weight/self.age)*10
    return speed
  # fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.
  def fight(self,other_dog):
    power_dog_1 = self.run_speed() * self.weight
    power_dog_2 = other_dog.run_speed() * other_dog.weight

    if power_dog_1 > power_dog_2:
      return self.name
    elif power_dog_2 > power_dog_1: # the elif is redundant change it to else
      return other_dog.name

dog_1 = Dog('shlomi',4,5)
dog_2 = Dog('gal',1,3)
dog_3 = Dog('tzif',6,8)

print(dog_1.bark())
print(dog_2.run_speed())
print(dog_1.fight(dog_3))

# create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method,
# this attribute is a boolean and the value should be False by default.
class PetDog(Dog):
  def __init__(self,name,age,weight,trained = False):
    super().__init__(name,age,weight)
    # Dog.__init__(name,age,weight)
    self.trained = trained
# train: prints the output of bark and switches the trained boolean to True
  def train(self):
    print(self.bark())
    self.trained = True 
# play: takes a parameter which value is a few names of other Dog instances (use *args).
# The method should print the following string: “dog_names all play together”.
  def play(self,*args):
    string = ''
    if not args:
      string = f'{self.name} is playing by himself!'
    else:
      for dog in args:
        if string == '':
          string = dog.name
        else:
          string = string + ", " + dog.name
      string = string + f' and {self.name} are playing together!'
    return string
# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.
  def do_a_trick(self,type = False):
    trick_list = ['barrel roll','spin','stand','paw']
    trick = ''
    if self.trained:
      if not type:
        trick = random.randint(0,len(trick_list))
      elif type in trick_list:
        trick = trick_list.index(type)
      string = f' look {self.name} is doing a {trick_list[trick]}'
    else:
      string = f'{self.name} is not trained'
    return string

    

t_dog_1 = PetDog('shlomi',4,5)
t_dog_2 = PetDog('yaniv',1,4)
print(t_dog_1.play())
print(t_dog_1.play(t_dog_2))

print(t_dog_1.do_a_trick())
t_dog_1.train()
print(t_dog_1.do_a_trick())
