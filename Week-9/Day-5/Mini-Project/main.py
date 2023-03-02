import random
blood_types= ['A','B','AB','O']

def check_type(blood_type):
  while blood_type not in blood_types:
    blood_type = input(f"Please choose your blood type: {' '.join(blood_types)} \n ").capitalize()
  return blood_type

def get_queue(queue_obj):
        Queue_list = []
        for person in queue_obj.humans:
         Queue_list.append(person.name)
        return Queue_list  

def shuffle_list(list):
  i = 0
  for index,human in enumerate(list):
    if human != list[-1]:
      if human in list[index+1].family:
        i+=1
        print(i)
  return i
  
class Human:
  def __init__(self,id:str,name:str,age:int,priority:bool,blood_type:str):
    self.id         = id
    self.name       = name
    self.age        = age
    self.priority   = priority
    self.blood_type = check_type(blood_type)
    self.family     = []
    print(self.id,self.name,self.age,self.priority,self.blood_type,self.family)

  def add_family_member(self,person):
    self.family.append(person)
    person.family.append(self)
    print(f'{self.name} and {person.name} live in the same house')


class Queue:
  def __init__(self,humans:list = []):
    self.humans = humans
    print(self.humans)

  def add_a_person(self,person:Human):
    if person.age >= 60 or person.priority:
      self.humans.insert(0,person)
      print(f'{person.name} was added to the start of the line!')
    else:
      self.humans.append(person)
      print(f'{person.name} was added to the end of the line!')
      
    return get_queue(self)

  def find_in_queue(self,person:Human):
    if person in self.humans:
      index = self.humans.index(person)
      return index
    return False #if person not in queue

  def swap_places(self,person_1:Human, person_2:Human):
    if person_1 in self.humans and person_2 in self.humans:
      index_1 = self.humans.index(person_1)
      index_2 = self.humans.index(person_2)

      self.humans[index_1] = person_2
      self.humans[index_2] = person_1
      
      Queue_list = get_queue(self)
      print(f'{person_1.name} and {person_2.name} swapped places!')
      print(Queue_list)
      return True
    return False

  def get_next(self):
    if len(self.humans) > 0:
      person = self.humans[0]
      self.humans.remove(person)
      return person.name
    else:
      return None

  def get_next_blood_type(self,type):
    type = check_type(type)
    for index,human in enumerate(self.humans):
      if human.blood_type == type:
        person = human
        self.humans.remove(human)
        return person.name
    return None

  def sort_by_age(self):
    self.humans.sort(key=lambda x: (x.priority == True ,x.age),reverse=True)
    return get_queue(self)

  def rearange_queue(self):
    while True:
      i = shuffle_list(self.humans)
      if i == 0:
        return get_queue(self)
      else:
        random.shuffle(self.humans)
        
        
my_human = Human('1111','David',42,False,'O')
my_human_2 = Human('2222','Yossi',62,True,'A')
my_human_3 = Human('3333','Daniel',93,False,'A')
my_human_4 = Human('4444','Mariza',21,True,'O')


Vaccine_Queue = Queue([my_human,my_human_2,my_human_3,my_human_4])


# Vaccine_Queue.swap_places(my_human,my_human_2)
# print(Vaccine_Queue.get_next_blood_type('O'))
# print(Vaccine_Queue.get_next())
print(Vaccine_Queue.sort_by_age())

my_human.add_family_member(my_human_3)
my_human_2.add_family_member(my_human_4)
print(Vaccine_Queue.rearange_queue())
