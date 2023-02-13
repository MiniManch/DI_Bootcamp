# Exercise Gold
# Create a function that will simulate the rolling of a dice. Call it throw_dice. It should return an integer between 1 and 6.
import random
def throw_a_dice():
  dice = random.randint(1,6)
  return dice
# Create a function called throw_until_doubles.
# It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number, ie. until we reach doubles.
def throw_until_doubles():
  dice_1  = throw_a_dice()
  dice_2  = throw_a_dice()
  attempt = 1
  while dice_1 != dice_2:
    dice_1   = throw_a_dice()
    dice_2   = throw_a_dice()
    attempt += 1
  return dice_1 , dice_2 , attempt
# For example: (1, 2), (3, 1), (5,5) → then stop throwing, because doubles were reached.
# This function should return the number of times it threw the dice in total. In the example above, it should return 3.

# Create a main function.
# It should throw doubles 100 times (ie. call your throw_until_doubles function 100 times), and store the results of those function calls (in other words, how many throws it took until doubles were thrown, each time) in a collection. (What kind of collection? Read below to understand what we will need the data for, and this should help you decide which data structure to use).
def main():
  i = 0
  result_list = []
  while i <100:
    result_list.append(throw_until_doubles()[2])
    i+=1
  avg = round(sum(result_list)/len(result_list),3)
  result_list.sort()
  print(f'Average throws to reach doubles: {avg} \n max number of throws it took : {result_list[-1]}')
# After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
# Also print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.

# Then my output would show something like this:
# Total throws: 8
# Average throws to reach doubles: 2.67.
main()
