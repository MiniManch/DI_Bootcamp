# # Exercise 1
# my_fav_numbers = {1,7,11,22,15,4}
# my_fav_numbers.add(14)
# print(my_fav_numbers)
#
# friend_fav_numbers = {5,18,23}
#
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
#
# print(our_fav_numbers)
#
# # Exercise 2
# # Q Given a tuple which value is integers, is it possible to add more integers to the tuple?
# # A you cannot change a tuple :(
#
# # Exercise 3
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# # Remove “Banana” from the list.
# # Remove “Blueberries” from the list.
# # Add “Kiwi” to the end of the list.
# # Add “Apples” to the beginning of the list.
# # Count how many apples are in the basket.
# # Empty the basket.
# # Print(basket)
# banana = "Banana"
# # 1
# basket.remove(banana)
#
# # 2
# bb = "Blueberries"
# basket.pop(basket.index(bb))
#
# # 3
# kiwi = "Kiwi"
# basket.append(kiwi)
#
# # 4
# apples = "Apples"
# basket.insert(0, apples)
#
# # 5
# basket.count(apples)
#
# # 6
# basket = []
#
# # 7
# print(basket)
#
# # Exercise 4
# # Recap – What is a float? What is the difference between an integer and a float?
# # Can you think of another way to generate a sequence of floats?
# # Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
#
# # 1
# # float is any number with a decimal point, even 4.0 is a float.
#
# # 2
# # I dont really understand this question honestly
#
# # 3
#
# i = 1.5
# list = []
#
# while i < 5.5:
#     if (i -  int(i)) > 0:
#         list.append(i)
#         i+=0.5
#     else:
#         list.append(int(i))
#         i+=0.5
#
# print(list)
#
# # Exercise 5
# # Use a for loop to print all numbers from 1 to 20, inclusive.
# # Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
#
# # 1
# for i in range(0,21):
#     print(i)
#
# # 2
# for i in range(0,21):
#     if (i % 2 == 0):
#         print(i)
#
# # Exercise 6
# # Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
#
# name = 'emmanuel'
# userName = input('Whats your name?').lower()
# while name != userName:
#     userName = input('wrong! try again')
# if name == userName:
#     print('thats the one!')
#
# # Exercise 7
#
# # Ask the user to input their favorite fruit(s) (one or several fruits).
# # Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# # Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# fav_fruit_list = input('What is your favourite fruit? if you have a few please divide them by commas ",": ').split(",")
# print(fav_fruit_list)
#
# # Now that we have a list of fruits, ask the user to input a name of any fruit.
# # If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# # If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
# userFruit = input('choose a fruit: ')
#
# if fav_fruit_list.count(userFruit) > 1:
#     print('You chose one of your favorite fruits! Enjoy!')
# else:
#     print('You chose a new fruit. I hope you enjoy')

# # Exercise 8
# # Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# # Went alittle overboard
#
# topping_av = ['Pepperoni','Mushroom','Extra cheese','Sausage','Onion','Black olives','Green pepper','Fresh garlic','Tomato','Fresh Basil']
# toppings   = []
# exit       = True
# print('Welcome to my Pizza Shop!')
# print('these are the toppings we have available for you today!')
# while exit:
#     if len(toppings) == len(topping_av):
#         print('we dont really know how we will fit all this on one pizza.. \n we will make it work')
#         exit = False
#     elif len(toppings) > 0:
#         print('anything else you would like to add? we have:')
#     copy_topping_av = topping_av.copy()
#     for n in toppings:
#         if n in copy_topping_av:
#             copy_topping_av.remove(n)
#     print(','.join(copy_topping_av))
#     new_topping = input('What would you like to add to your pizza?: ').lower().capitalize()
#     while copy_topping_av.count(new_topping.lower().capitalize()) == 0:
#         new_topping = input(f"we dont seem to have that, pick something from the list!\n here is the list again: {(','.join(copy_topping_av))}\n").lower().capitalize()
#     toppings.append(new_topping)
#     out = input('if this is the only topping(s) you want on your pizza, please enter "exit". \n otherwise, just click enter! \n or write whatever \n do i look like i care? ')
#     if out == 'exit':
#         exit = False
#
# # As they enter each topping, print a message saying you’ll add that topping to their pizza.
# # Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
# price                   = 10 + len(toppings)*2.5
# list_of_toppings_chosen = ','.join(toppings)
# print(f"the toppings you chose are {list_of_toppings_chosen}. the total price is: {price}$ ")



# Exercise 10 +Exercise 11
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
sandwich_orders.append('Pastrami sandwich')
sandwich_orders.append('Pastrami sandwich')

print('oh no we ran out of pastrami!')

pastrami = "Pastrami sandwich"
while pastrami in sandwich_orders:
    sandwich_orders.remove(pastrami);
print(pastrami)
# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
finished_sandwiches = []
# As each sandwich is made, move it to the list of finished sandwiches.
list_of_sand   = ','.join(sandwich_orders)
print('we have: ,',list_of_sand)
exit = True
while exit:
    # if we're first running this loop the text should say this in the input
    copy_list_sand = sandwich_orders.copy();
    string_options = ','.join(copy_list_sand);
    if len(finished_sandwiches) == 0:
        userSandChoice = input(f'What would you like us to make for you? \n we have: (enter exit to quit) {list_of_sand}\n').lower().capitalize();
        if userSandChoice.lower() == 'exit':
            print('so you dont want anything?')
            break
            # exit = False
            # if exit == False:
            #     break
    elif len(finished_sandwiches) == len(sandwich_orders):
        print(' we dont have anything else. thats it. you have it all')
        # exit = False
        break
    else:
        # function to take out of the options what the user chose
        for n in finished_sandwiches:
            if n in copy_list_sand:
                copy_list_sand.remove(n)
        string_options = ','.join(copy_list_sand);
        userSandChoice = input(f'would you like something else? \n we have: \n {string_options} \n').lower().capitalize();
    # checking if the item is in the list of items available
    while userSandChoice not in copy_list_sand:
        userSandChoice = input(f'we dont have that, we have \n we have: \n {string_options} \n').lower().capitalize();
    finished_sandwiches.append(userSandChoice)
    # IDK why but ,flags only break the loop at the end, so using break makes more sense since
    # i had to add another if statement to break it then and not ask another question
    # if exit == False:
    #     break
    # input for exit the loop (flag)
    done = input('is that all? enter "exit" if so')
    if done.lower() == 'exit':
        # exit = False
        break
for i in finished_sandwiches:
    print(f'I have made you a {i}')
