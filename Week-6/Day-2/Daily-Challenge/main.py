# Daily Challenge
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

# Then, print the first and last characters of the given text.

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
import random

userString = input('Give me some wordssss: ')
if len(userString) > 10:
  print('String is too long!')
elif len(userString) < 10:
  print('String is too short!')
else:
  print('uhh yeah, just right')
  print(
    f'the first letter is {userString[0]} and the last letter is {userString[len(userString)-1]}'
  )
  i = 0
  list = []
  for x in range(len(userString) + 1):
    sliceObj = slice(0, i)
    print(userString[sliceObj])
    i += 1
    if x <= len(userString) - 1:
      list.append(userString[x])
  random.shuffle(list)
  shuffleString = ''.join(list)
  print(shuffleString)


  
