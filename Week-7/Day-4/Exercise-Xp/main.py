# Exercise 1
import random
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().
# Bonus: Give the temperature as a floating-point number instead of an integer.



def get_random_temp():
  season_dict = {
    'summer': (20, 40),
    'winter': (-10, 15),
    'fall': (16, 25),
    'spring': (10, 20)
  }
  season_keys_list = season_dict.keys()
  season_list_String = ','.join(season_keys_list)
  season = input(
    f'Please provide a season! \n Choose one of the following:\n {season_list_String} \n'
  ).lower()
  while season not in season_keys_list:
    print('idk what you entered but thats not a viable season')
    season = input(
      f'Please provide a season! \n Choose one of the following:\n {season_list_String} \n'
    ).lower()
  if season == 'summer':
    rand_temp = round(random.uniform(season_dict['summer'][0],
                               season_dict['summer'][1]),2)
  elif season == 'autumn' or season == 'fall':
    rand_temp = round(random.uniform(season_dict['fall'][0],
                               season_dict['fall'][1]),2)
  elif season == 'winter':
    rand_temp = round(random.uniform(season_dict['winter'][0],
                               season_dict['winter'][1]),2)
  else:
    rand_temp = round(random.uniform(season_dict['spring'][0],
                               season_dict['spring'][1]),2)
  return rand_temp, season


# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40


def main():
  rand_temp = get_random_temp()
  print(f'The temperature right now is {rand_temp[0]} degrees Celsius.')
  if rand_temp[0] <= 0:
    print('Brrr, that’s freezing! Wear some extra layers today')
  elif rand_temp[0] > 0 and rand_temp[0] < 16:
    print('Quite chilly! Don’t forget your coat')
  elif rand_temp[0] >= 16 and rand_temp[0] <= 23:
    print('Thats alittle cold, a sweater would do you right!')
  elif rand_temp[0] >= 24 and rand_temp[0] < 32:
    print('Thats perfect! short sleeve weather')
  else:
    print('thats so hot!')


main()

# Exercise 2
# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947).
# Create a function get_age(year, month, day)

# Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
# After calculating the age of a person, the function should return the age (the age is an integer).
import datetime
today = datetime.date.today()
year = today.year

# Create a function get_age(year, month, day)
#Didnt understand why should i get month and day if age is an integer.
def calc_age():
  user_year_of_birth = input('Please enter what year you were born in! \n ')
  while not user_year_of_birth.isnumeric():
    user_year_of_birth = input('thats a wrong input! \n Please enter what year you were born in! \n ')
  user_year_of_birth = int(user_year_of_birth)

  user_age = year - user_year_of_birth
  return user_age

# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age.
# Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
 # Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.
# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message informing the user whether they can retire or not.
# As always, test your code to ensure it works.

def can_retire():
  user_age = calc_age()
  user_gender = input('Whats your gender? please enter f or m accordingly! \n')
  gender_list = ['f','m']
  while user_gender not in gender_list:
    user_gender = input('Whats your gender? please enter f or m accordingly! \n')
  if user_gender == 'f':
    retirement_age = 62
  else:
    retirement_age = 67

  return user_age >= retirement_age, retirement_age - user_age

result =  can_retire()
if result[0]:
  print('Yay you can retire, lets go!!!')
else:
  print(f'sorry you gotta work {result[1]} more years!')
  

# Exercise 3 
# Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example:
# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)

# Hint: treating our number as a int or a str at different points in our code may be helpful
def i_like_this_number():
  user_number  = input('Give me a number please: \n')
  while  not user_number.isnumeric():
    user_number  = input('Give me a number please: \n')
  calc = (user_number) + '+' + user_number * 2 + '+' + user_number * 3 + '+' + user_number*4
  final = eval(calc)
  return final 

print (i_like_this_number())