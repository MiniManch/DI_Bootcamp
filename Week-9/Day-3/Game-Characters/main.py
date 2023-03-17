import random

class Character:
  class_name = None
  def __init__(self,name):
    self.name       = name
    self.health     = 20
    self.attack     = 10

  def basic_attack(self,other_char):
    other_char.health -= self.attack

  def __gt__(self,other):
    this_char = type(self).class_name
    other_char = type(other).class_name

    if this_char  == 'Mage' and other_char != 'Mage':
      return True
    if this_char == 'Druid' and other_char == 'Warrior':
      return True
    return False

  def info(self):
    return {'Health':self.health,'Attack':self.attack}

  # @classmethod
  # def __str__(cls):
  #   return cls.class_name

class Druid(Character):
  class_name = 'Druid'
  move_list  = ['help','meditate','animal_help','drain','attack']
  move_on_enm = 'drain'

  def __init__(self,name):
    super().__init__(name)
    print('Im a druid, get ready to die !')

  def meditate(self):
    self.health += 10
    print(f'{self.name} meditated 🧎‍ hes calm now, and his health has increased by 10 ✨')

  def animal(self):
    self.attack += 5
    print(f'{self.name} has used Animal Help 🐾 his attack has increased by 5')

  def drain(self,other_char):
    attack = self.health * 0.75 + self.attack * 0.75
    other_char.health -= attack
    print(f'{self.name} has deal {attack} amount of damage on {other_char.name} 💢')

  def help(self):
    return f' {self.name} You can use -attack-, -drain-, get an -animal- to help you, or -meditate-'


class Warrior(Character):
  class_name = 'Warrior'
  move_list  = ['help','brawl','train','intimidate','attack']
  move_on_enm = ['brawl','intimidate']

  def __init__(self,name):
    super().__init__(name)
    print('Im a warrior 👨‍🎤 this will be easy!')

  def brawl(self,other_char):
    other_char.health -= self.attack * 2
    self.health += self.attack * 0.5
    print(f'{other_char.name} has been dealt {self.attack * 2} damage! 💢')
    print(f'and {self.name} health has increased by {self.attack * 0.5}')

  def train(self):
    self.health += 2
    self.attack += 2
    print(f'{self.name} used train. 🏋️‍ his attack and health are now increased by 2!')

  def intimidate(self,other_char):
    other_char.attack -= 3
    print(f'{self.name} just flashed his muscles 🦾 theyre so big, that {other_char.name} damage has decreased by 3')

  def help(self):
    return f' {self.name} you can try and -intimidate- the enemy,-train- to increase your strength, simply -attack-, or try get in a -brawl-'


class Mage(Character):
  class_name = 'Mage'
  move_list  = ['help','cast','summon','curse','attack']
  move_on_enm = ['curse','cast']
  def __init__(self,name):
    super().__init__(name)
    print('being a mage 🧙‍ I can forsee exactly how this battle will pan out!')
    
  def curse(self,other_char):
    other_char.attack -= 2
    print(f'{self.name} cursed {other_char.name}  \n {other_char.name} is insulted 🥺. his attack has decrseased by 2')

  def summon(self):
    self.attack += 3
    print(f'{self.name} has summoned a monster 👹 \n he can attack exactly +3 harder now')

  def cast(self,other_char):
    attack = self.health/self.attack
    other_char.health -= attack
    print(f'{self.name} just cast a spell 🌪 \n {other_char.name}\'s health just decreased by {attack}')

  def help(self):
    return f' {self.name} You can -Cast- a spell, -summon- a monster,attack or -curse- the enemy!'

def choose_char():
  char_list = [Mage,Warrior,Druid]
  player_list = ['player_1','player_2']

  for index,player in enumerate(player_list):
    player_name = input('Hey there, please choose a name \n')
    while type(player_list[0])!= str:
      while player_name == player_list[0]['Name']:
        player_name = input('Hey there, please choose a name \n')
      break
    player_char = input(f'Hey {player_name}, please choose a Character! (Mage,Warrior or Druid) \n').lower().capitalize()

    i = True
    counter = 0
    while i == True:
      for char_type in char_list:
        if counter == len(char_list):
          player_char = input(f'Hey {player_name}, please choose a Character! (Mage,Warrior or Druid) \n').lower().capitalize()
          counter = 0
        if player_char == char_type.class_name:
          player_char = char_type(player_name)
          i = False
        counter +=1

    player = {'Name':player_name,'Char':player_char}
    player_list[index] = player
  return player_list


# change turns decide who starts, perhaps make it logical based on char type
def first_turn(player_list):
  this_char  = player_list[0]['Char']
  other_char = player_list[1]['Char']

  if this_char > other_char and other_char > this_char:
    return 0
  return random.randint(0,1)  

# if health is 0 winner is declared
def play(turn,player_list,attack,health,name,char):  
  print(f'{name} its your turn! \n you have Attack of:{attack} and Health of {health}')
  choice = input(f"{name}\n {char.help()} \n").lower()
  while choice not in char.move_list:
    choice = input(f"{name}\n {char.help()} \n").lower()
  return choice

def check_win(player_list):
  for player in player_list:
    if player['Char'].health == 0:
      return True
  return False


def game():
  player_list = choose_char()
  turn = first_turn(player_list)
  while not check_win(player_list):
    if turn == 0:
      other_char = 1
    elif turn ==1:
      other_char = 0

    info = player_list[turn]['Char'].info()
    attack = info['Attack']
    health = info['Health']
    name   = player_list[turn]['Name']
    char   = player_list[turn]['Char']
    other_char = player_list[other_char]['Char']

    print('other',char)
    choice = play(turn,player_list,attack,health,name,char)
    if choice == 'attack':
      eval(f'{char}.basic_attack({other_char})')
    if choice in type(char).move_on_enm:
      eval(f'{char}.{choice}({other_char})')
    else:
      exec(f'{char}.{choice}()')

    if turn == 0:
      turn = 1
    elif turn == 1:
      turn = 0


  return choice

print(game())
  
