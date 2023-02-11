# Exercise Gold
# Exerise 1 + Exercise 2 + Exercise 3
# from dateutil import parser
from datetime import datetime
# Create a variable called birthdays. Its value should be a dictionary.
# Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
birthdays = {
  'Emmanuel': '1996/05/02',
  'Adi': '1995/27/12',
  'Yossi': '1994/27/04',
  'Dominique': '1967/11/02',
  'David': '1959/04/03'
}

# Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“

# Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
# Ask the user for a person’s name – store it in a variable.
# Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# Now add this new data into your dictionary.
# Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.

check = input('wanna add someone to the birthday list? format yyyy/dd/mm \n')
format = "%Y/%d/%m"

res = False

while not res:
  if check.lower() == 'no':
    print('Well thats it folks')
    break
  try:
    res = bool(datetime.strptime(check, format))
  except ValueError:
    res = False
    check = input(
      'try again, it needs to be in appropriate format\n yyyy/dd/mm \n')

if check.lower() != 'no':
  new_name = input('and whos birtday is that? \n').lower().capitalize()
  if new_name not in birthdays.keys():
    birthdays[new_name] = check
  else:
    print(f'{birthdays[new_name]} thats {new_name}s birthday!')

birthdays_keys_string = ','.join(birthdays.keys())

print(
  f'Hey there user! \n we can look for a birthday for you\n you can ask for any of the following:\n{birthdays_keys_string}'
)
# Ask the user to give you a person’s name and store the answer in a variable.
user_input_bd = input(
  'Wanna get a birthday of someone from the list?(enter no to quit)\n').lower(
  ).capitalize()
# Get the birthday of the name provided by the user.
while user_input_bd not in birthdays.keys():
  if user_input_bd == 'No':
    print('thats it folks')
    break
  user_input_bd = input(
    f' {user_input_bd} is not in the list, try again\n').lower().capitalize()
# Print out the birthday with a nicely-formatted message.
if user_input_bd != 'No':
  print(
    f'He/she were born in {birthdays[user_input_bd][0:4]}\n on the {birthdays[user_input_bd][5:7]}th day of the {birthdays[user_input_bd][8:]} month!'
  )

# Exercise 4
items = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
# Using the dictionary above, each key-value pair represents an item
# and its price - print all the items and their prices in a sentence.
for item in items:
  print(f"we have {item}. it costs {items[item]}$")
# Using the dictionary below, each value are dictionaries containing both the price
# and the amount of items in stock -
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}
# write some code to calculate how much it would cost to buy everything in stock.
sum = 0
for item in items:
  total_cost = items[item]["price"] * items[item]['stock']
  sum += total_cost
print(sum,'$')