# In a file named func.py create a function that adds 2 number, and prints the result
from func import add_two_nums as add_two
# In a file namedexercise_one.py import and the function
print(add_two(8,9))

import random
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.
def guess_till_hundred(user_num):
  computer_num = random.randint(1,100)
  if user_num == computer_num:
    print('success')

# Generate random String of length 5
import string

my_string = ''
all_letters = string.ascii_letters
for index in range(0,5):
  my_string = my_string + all_letters[random.randint(1,len(all_letters )- 1)]

print(my_string)

# Create a function that displays the current date.
# Hint : Use the datetime module.
from datetime import date,datetime
today_date_time = datetime.today()
today_date = date.today()

print("Today's date:", today_date)

# Create a function that displays the amount of time left from now until January 1st.
jan_first = datetime(2024,1,1)
print(jan_first - today_date_time)

# Create a function that accepts a birthdate as an argument 
# in the format of your choice),
# then displays a message stating how many minutes the user lived in his life.
def how_many_minutes_you_lived():
  year = int(input('please enter what year you were born in \n'))
  day = int(input('please enter what day you were born in \n'))
  month = int(input('please enter what month you were born in \n'))

  birthday = date(year,month,day)
  timesince = today_date - birthday
  minutessince = int(timesince.total_seconds() / 60)

  return minutessince
print(how_many_minutes_you_lived())


# The function should  display the amount of time left from now until the next upcoming holiday and print which holiday that is.
passover = datetime(2023,4,15)
timesince = passover - today_date_time
print(timesince)

# Given an age in seconds, calculate how old someone would be on planets

planet_dict = {'Earth':1,
               'Mercury': 0.2408467,
               'Venus'  : 0.61519726,
               'Mars'   : 1.8808158,
               'Jupiter': 11.862615,
               'Saturn' : 29.447498,
               'Uranus' : 84.016846,
               'Neptune': 164.79132}
earth_sec_year   = 31557600 

for planet in planet_dict:
  planet_dict[planet] = earth_sec_year * planet_dict[planet]

def how_old_in_planets(age_in_sec):
  for planet in planet_dict:
    print(f'you are {age_in_sec/planet_dict[planet]} in {planet}')

how_old_in_planets(1000000000)

# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.


# pip install Faker
from faker import Faker

fake = Faker()
users = []
def add_new_fake_user(user_list):
  user = {'Name'      : fake.name(),
          'Address'   : fake.address(),
          'Lang_Code' : fake.language_code()}
  user_list.append(user)

add_new_fake_user(users)
add_new_fake_user(users)
add_new_fake_user(users)
add_new_fake_user(users)
add_new_fake_user(users)

print(users)