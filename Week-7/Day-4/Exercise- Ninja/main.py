# Exercise 1 : What’s Your Name ?
# Instructions
# Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.
def get_full_name(f_name, l_name, *args):
  name_list = [f_name, l_name]
  for name in list(args):
    name_list.append(name)
  full_name_String = ' '.join(name_list)
  print(f' Oh so your full name is {full_name_String}!')


get_full_name('Emmanuel', 'Rokah', 'Lopez', 'Cohen', 'Bahar')
get_full_name(f_name="bruce", l_name="lee")

# Exercise 2 : From English To Morse
# Write a function that converts English text to morse code and another one that does the opposite.
# Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash

MORSE_CODE_DICT = {
  'A': '.-',
  'B': '-...',
  'C': '-.-.',
  'D': '-..',
  'E': '.',
  'F': '..-.',
  'G': '--.',
  'H': '....',
  'I': '..',
  'J': '.---',
  'K': '-.-',
  'L': '.-..',
  'M': '--',
  'N': '-.',
  'O': '---',
  'P': '.--.',
  'Q': '--.-',
  'R': '.-.',
  'S': '...',
  'T': '-',
  'U': '..-',
  'V': '...-',
  'W': '.--',
  'X': '-..-',
  'Y': '-.--',
  'Z': '--..',
  '1': '.----',
  '2': '..---',
  '3': '...--',
  '4': '....-',
  '5': '.....',
  '6': '-....',
  '7': '--...',
  '8': '---..',
  '9': '----.',
  '0': '-----',
  ', ': '--..--',
  '.': '.-.-.-',
  '?': '..--..',
  '/': '-..-.',
  '-': '-....-',
  '(': '-.--.',
  ')': '-.--.-'
}


def english_to_morse():
  morse_keys = MORSE_CODE_DICT.keys()
  try:
    user_input = input(
      'Give me an english string I will translate to morse! \n').upper()
    print(user_input)
  except:
    print('error')
  cipher = ''    
  for letter in user_input:
    if letter != ' ':
      if letter not in morse_keys:
        return 'wrong key'
      # Looks up the dictionary and adds the
      # corresponding morse code
      # along with a space to separate
      # morse codes for different characters
      print(letter)
      cipher += MORSE_CODE_DICT[letter] + '/'
    else:
      # 1 space indicates different characters
      # and 2 indicates different words
      print(letter)
      cipher += ' '

  return cipher


print(english_to_morse())
