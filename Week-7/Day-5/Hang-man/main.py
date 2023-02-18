import random

wordslist = [
  'correction', 'childish', 'beach', 'python', 'assertive', 'interference',
  'complete', 'share', 'rush', 'south'
]


def wanna_play():
  while True:
    #for some reason when I did while user_want != 'no' or 'yes' it just entered the loop anyway, so this way works 100%
    user_want = input(
      'Wanna play hangman? \n enter yes to play and no to stop! \n').lower()
    if user_want == 'yes':
      user_want = True
      break
    elif user_want == 'no':
      user_want = False
      break
  return user_want


def get_random_word():
  word = random.choice(wordslist)
  hidden_word = '*' * len(word)
  return word, hidden_word


def take_a_guess(letter_list):
  letters_left = letter_list
  user_guess = input(
    f'Please enter a letter! the remaining letters are: \n {letter_list} \n')
  while True:
    if len(user_guess) > 1 and user_guess not in letters_left:
      user_guess = input(f'Try again, the remaining letters are: \n {letter_list} \n ')
    break
  print('yello')
  return user_guess

def word_list_creator(word):
  word_list = []
  for star in word:
    word_list.append(star)
    
  return word_list
  
def lets_play():
  if not wanna_play():
    print('Youre a bummer')
    return False
  words = get_random_word()
  word_stars = words[1]  
  word_to_guess = words[0]
  
  print(f'time to start guessing, the word to guess is: \n {word_stars}')

  word_stars_list = word_list_creator(word_stars)
  
  failed_guess_list    = []
  letters_left         = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
  
  while True:
    # check if win or lose
    if word_stars == word_to_guess:
      print('You guessed it! youre a winner!')
      return True
    elif len(failed_guess_list) == 5:
      print('Fail! total fail. you lose! the hangman died. its your fault ')
      return False
    user_guess = take_a_guess(letters_left)
    letters_left = letters_left.replace(user_guess,'')
    if user_guess in word_to_guess:
      for index,letter in enumerate(word_to_guess):
        if letter == user_guess:
          word_stars_list[index] = user_guess
      word_stars = ''.join(word_stars_list)
      
    else:
      failed_guess_list.append(user_guess)
    print(f' you already tried: {failed_guess_list}')
    print(word_stars)
        
lets_play()