import random

class Game:
  def __init__(self):
    self.possible_moves = ['Rock','Paper','Scissors']
    self.wins           = ['RockScissors','PaperRock','ScissorsPaper']
    self.results = {'win':0,'loss':0,'draw':0}
  
    
  def get_user_move(self):
    self.user_move = input('Please choose your move!\n you can choose either Rock,Paper or Scissors \n').lower().capitalize()
    while self.user_move not in self.possible_moves:
      self.user_move = input('Please choose your move!\n you can choose either Rock,Paper or Scissors \n').lower().capitalize()
    return self
    
  def get_computer_move(self):
    self.computer_move = random.choice(self.possible_moves)
    return self

  def get_game_result(self):
    if self.user_move == self.computer_move:
      self.results['draw'] += 1
      return 'OH! its a draw'
    elif  self.user_move + self.computer_move in self.wins:
      self.results['win'] += 1
      return 'you win!'
    else:
      self.results['loss'] += 1
      return 'you lose'

  def play(self):
    self.get_user_move()
    self.get_computer_move()

    print(f'You chose {self.user_move}')
    print(f'The computer chose {self.computer_move}')
    print(self.get_game_result())
    
    
# RPS.play()
