# Exercise 1
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
def display_message():
  print(
    'We are learning how to develop websites using: \n HTML,CSS,JS Python and more!'
  )


# Call the function, and make sure the message displays correctly.

display_message()


# Exercise 2
# Write a function called favorite_book() that accepts one parameter called title.
def favorite_book(title='Harry Potter'):
  print(f'one of my favorite books is {title}')


# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.
favorite_book('Alice in Wonderland')


# Exercise 3
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
def describe_city(city_name, country='Israel'):
  print(f'{city_name} is in {country}')


# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
describe_city('Nathanya')

# Exercise 4
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
import random


def random_int_1_till_100(num):
  while type(num) != int:
    num = input('Please provide an integer \n')
    if num.isnumeric():
      num = int(num)
  randnum = random.randint(1, 100)

  if num == randnum:
    print('sucess!')
  else:
    print(f'Fail! your number is {num} and the randomized number is {randnum}')


random_int_1_till_100('w')

# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
# Call your function.


# Exercise 5
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
def make_shirt(size, message):
  print(f'The size of the shirt is {size} and the text is {message}')


# Call the function make_shirt().


# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
def make_shirt(size='large', message='I love Python'):
  print(f'The size of the shirt is {size} and the text is {message}')


# Make a large shirt with the default message
# Bonus: Call the function make_shirt() using keyword arguments.

make_shirt()
# Make medium shirt with the default message
make_shirt('medium')
# Make a shirt of any size with a different message.
make_shirt(message='We are man united and we are going to wembely')

# Exercise 6
# Using this list of magician’s names.
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
def show_magicians(list):
  for item in list:
    print(item)
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
def make_great(list):
  for index, item in enumerate(list):
    list[index] = item + ' the Great'
# Call the function make_great().
make_great(magician_names)
# Call the function show_magicians() to see that the list has actually been modified.
show_magicians(magician_names)
