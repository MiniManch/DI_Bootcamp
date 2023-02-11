confirm = input(
  'pssst do you wanna encrypt a code? i can also decrypt.\n enter y for encryption and x for the opposite!\n'
)
cesar_word_list = []
de_or_e = 3
while confirm == 'x' or confirm == 'y':
  if confirm == 'x':
    print('pssst you chose decryption!')
    de_or_e = -3
  elif confirm == 'y':
    print('pssst you chose encryption!')
  user_word = input(
    'pssst... give me a string, ill do what needs to be done. \n')
  for letter in user_word:
    cesar_word_list.append(chr(ord(letter) + de_or_e))
  break

if len(cesar_word_list) > 0:
  cesar_word = ''.join(cesar_word_list)
  print(f'your encrypted string is {cesar_word}')
else:
    print('you chose: nothing. ok.')

#If we use this system we get instances like ` and ^
# and when we try to decrypt that we get errors.
