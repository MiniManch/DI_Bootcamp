# Exercise 1
my_fav_numbers = {1,7,11,22,15,4}
my_fav_numbers.add(14)
print(my_fav_numbers)

friend_fav_numbers = {5,18,23}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)

# Exercise 2
# Q Given a tuple which value is integers, is it possible to add more integers to the tuple?
# A you cannot change a tuple :(

# Exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
banana = "Banana"
# 1
basket.remove(banana)

# 2
bb = "Blueberries"
basket.pop(basket.index(bb))

# 3
kiwi = "Kiwi"
basket.append(kiwi)

# 4
apples = "Apples"
basket.insert(0, apples)

# 5
basket.count(apples)

# 6
basket = []

# 7
print(basket)

# Exercise 4
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

# 1
# float is any number with a decimal point, even 4.0 is a float.

# 2
# I dont really understand this question honestly

# 3

i = 1.5
list = []

while i < 5.5:
    if (i -  int(i)) > 0:
        list.append(i)
        i+=0.5
    else:
        list.append(int(i))
        i+=0.5

print(list)

# Exercise 5
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

# 1
for i in range(0,21):
    print(i)

# 2
for i in range(0,21):
    if (i % 2 == 0):
        print(i)

# Exercise 6
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

name = 'Emmanuel'
userName = input('Whats your name?')
while name != userName:
    userName = input('wrong! try again')

