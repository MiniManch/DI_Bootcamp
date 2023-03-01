class Character:
  def __init__(self,name):
    self.name   = name
    self.health = 20
    self.attack = 10

  def basic_attack(self,other_char):
    other_char.health -= self.attack


class Druid(Character):
  def __init__(self):
    print('Im a druid, get ready to die !')

  def meditate(self):
    self.health += 10
    print(f'{self.name} meditated 🧎‍♂️ hes calm now, and his health has increased by 10 ✨')

  def animal_help(self):
    self.attack += 5
    print(f'{self.name} has used Animal Help 🐾 his attack has increased by 5')

  def drain(self,other_char):
    attack = self.health * 0.75 + self.attack * 0.75
    other_char.health -= attack
    print(f'{self.name} has deal {attack} amount of damage on {other_char.name} 💢')

  def help(self):
    return f' {self.name} You can use drain(a), get an animal to help you(b), or meditate(c)'


class Warrior(Character):
  def __init__(self):
    print('Im a warrior 👨‍🎤 this will be easy!')

  def brawl(self,other_char):
    other_char.health -= self.attack * 2
    self.health += self.attack * 0.5
    print(f'{other_char.name} has been dealt {self.attack * 2} damage! 💢')
    print(f'and {self.name} health has increased by {self.attack * 0.5}')

  def train(self):
    self.health += 2
    self.attack += 2
    print(f'{self.name} used train. 🏋️‍♂️ his attack and health are now increased by 2!')

  def intimidate(self,other_char):
    other_char.attack -= 3
    print(f'{self.name} just flashed his muscles 🦾 theyre so big, that {other_char.name} damage has decreased by 3')

  def help(self):
    return f' {self.name} you can try and intimidate(a) the enemy,train(b) to increase your strength, try get in a brawl(c)'


class Mage(Character):
  def __init__(self):
    print('being a mage 🧙‍♂️ I can forsee exactly how this battle will pan out!')
    
  def curse(self,other_char):
    other_char.attack -= 2
    print(f'{self.name} cursed {other_char.name}  \n {other_char.name} is insulted 🥺. his attack has decrseased by 2')

  def summon(self):
    self.attack += 3
    print(f'{self.name} has summoned a monster 👹 \n he can attack exactly +3 harder now')

  def castspell(self,other_char):
    attack = self.health/self.attack
    other_char.health -= attack
    print(f'{self.name} just cast a spell 🌪 \n {other_char.name}\'s health just decreased by {attack}')

  def help(self):
    return f' {self.name} You can Cast a spell(a), summon a monster(b), or curse(c) the enemy!'


def choose_char():
  char_list = ['Mage','Warrior','Druid']
  player_list = ['player_1','player_2']

  for index,player in enumerate(player_list):
    player_name = input('Hey there, please choose a name \n')
    player_char = input(f'Hey {player_name}, please choose a Character! (Mage,Warrior or Druid) \n').lower().capitalize()
    while player_char not in char_list:
      player_char = input(f'Hey {player_name}, please choose a Character! (Mage,Warrior or Druid) \n').lower().capitalize()
    player_list[index] = {player:[player_name,player_char]}
  return player_list

def game():
  player_list = choose_char()

game()
  
