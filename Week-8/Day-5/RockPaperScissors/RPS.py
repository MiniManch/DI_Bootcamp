from game import *

def get_user_menu_choice():
  choice = input('Hey there! Wanna play some Rock,Papper,Scissors against me? \n choose (y) to play, (s) to show scores, and any other key to just stop! \n')
  return choice

def print_results(results:dict):
  print(f'''
        you won: {results['win']} games!
        you lost: {results['loss']} games!
        you drew: {results['draw']} games!
        ''')

def main():
  while True:
    user_choice = get_user_menu_choice()
    if user_choice.lower() == 'y':
      RPS.play()
    elif user_choice.lower() == 's':
      print_results(RPS.results)
    else:
      print('Bye!')
      break

RPS = Game()
main()