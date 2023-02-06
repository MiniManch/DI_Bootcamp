# Exercise 1
print(
  ' Hello World \n Hello World \n Hello World \n Hello World \n Hello World \n '
)

# Exercise 2
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
calc = (99**3) * 8
print(calc)

# Exercise 3
# >>> 5 < 3 false
# >>> 3 == 3 true
# >>> 3 == "3" false
# >>> "3" > 3  error
# >>> "Hello" == "hello" false

# Exercise 4
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

computer_brand = 'Lenovo'
print(f'I have a {computer_brand} computer')

# Exercise 5
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

name = 'Emmanuel'
age = '26'
shoe_size = '45'
info = 'I love Manchester United'

print(
  f'my name is {name}, I am {age} years old and my shoe size is {shoe_size}. You should know, {info}'
)

# Exercise 6
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.

a = 5
b = 6
if a > b:
  print('Hello World')
else:
  print("Bye world")

# Exercise 7
# Write code that asks the user for a number and determines whether this number is odd or even.

userNum = input('Give me a number person: ')
# in future should probably check if its a string or Nan value and then ask again for a number if it is.
if int(userNum) % 2 == 0:
  print('your number is even!')
else:
  print('your number is odd!')

# Exercise 8
# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

userName = input('What is your name mister? ')

if userName == name:
  print(
    'wow we have the same name, maybe we should do something later, get to know eachother better'
  )
else:
  print('your name is basic, sorry not sorry 😘')

# Exercise 9
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

userHeight = int(input('Please enter your height! in inches tho: '))

if userHeight * 2.54 >= 145:
  print('youre tall enough to ride, have a good time!')
else:
  print('youre too short, find something else to do')
