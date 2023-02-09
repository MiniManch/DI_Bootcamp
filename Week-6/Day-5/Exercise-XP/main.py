# # Exercise 1
# # Convert the two following lists, into dictionaries.
# # Hint: Use the zip method
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# new_list = list(zip(keys,values))
#
# # Exercise 2
# # A movie theater charges different ticket prices depending on a person’s age.
# # if a person is under the age of 3, the ticket is free.
# # if they are between 3 and 12, the ticket is $10.
# # if they are over the age of 12, the ticket is $15.
# # Given the following object:
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#
# # How much does each family member have to pay ?
# # ticket_price = 0;
# # sum = 0
# # for key in family:
# #     if family[key] > 0 and family[key] <= 3:
# #         ticket_price = 0;
# #     elif family[key] < 12:
# #         ticket_price = 10
# #     else:
# #         ticket_price = 15
# #     print(f"{key}'s price is : {ticket_price}");
# #     sum += ticket_price
# # print(f"the total price is: {sum}")
#
# # Print out the family’s total cost for the movies.
# # Bonus: Ask the user to input the names and ages instead of using the provided family variable
# # (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
# i = 0
# dict = {}
# while i <5:
#     name = input('SHOW ME WHAT YOU GOT')
#     age  = int(input('SHOE ME WHAT YOUR AGE'))
#     dict[name] = age
#     i+=1
#     print(i)
#
# ticket_price = 0;
# sum = 0
# for key in dict:
#     if dict[key] > 0 and dict[key] <= 3:
#         ticket_price = 0;
#     elif dict[key] < 12:
#         ticket_price = 10
#     else:
#         ticket_price = 15
#     print(f"{key}'s price is : {ticket_price}");
#     sum += ticket_price
# print(f"the total price is: {sum}")

# Exercise 3
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green
# Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
brand = {
    'name' : 'Zara',
    'creation_date' : 1975,
    'creator_name'  : 'Amancio Ortega Gaona',
    'type_of_clothes' : ['men','women','children','home'],
    'international_competitors' : ['Gap','H&M','Benetton'],
    'number_stores': 7000,
    'major_color' : {
        'France' : 'blue',
        'Spain': 'red',
        'US': ['pink','red']
    }
}

# 3. Change the number of stores to 2.
brand['number_stores'] = 2
# 4. Print a sentence that explains who Zaras clients are.
print(f"{brand['name']} has clotehes for {','.join(brand['type_of_clothes'])}")
# 5. Add a key called country_creation with a value of Spain.
brand['country_creation'] = 'spain'
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
int_comp = 'international_competitors'
if int_comp in list(brand.keys()):
    brand[int_comp].append('Desigual')
# 7. Delete the information about the date of creation.
brand.pop('creation_date')
# 8. Print the last international competitor.
print(brand['international_competitors'][-1])
# 9. Print the major clothes colors in the US.
print(brand["major_color"]['US'])
# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))
# 11. Print the keys of the dictionary.
print(','.join(list(brand.keys())))
# 12. Create another dictionary called more_on_zara with the following details:
# creation_date: 1975
# number_stores: 10 000
more_on_zara = {
    'creation_date' : 1975,
    'number_stores': 10000
}
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)
# 14. Print the value of the key number_stores. What just happened ?

print(brand['number_stores'])

# Exercise 4
# Use this list :
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Analyse these results :
# create a code to recreate these results
# #1
#
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p
users_copy = users.copy()
for elem in users_copy:
    if 'i' not in elem.lower() or elem[0].lower() != 'm' or elem[0].lower != 'p':
        users_copy.remove(elem)
print(users_copy)
num_list = [0,1,2,3,4]
list_1 = list(zip(users,num_list))
dict = {}
for i in list_1:
    dict[i[0]] = i[1]
print(dict)
#
# #2/
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
list_1 = list(zip(num_list,users))
dict = {}
for i in list_1:
    dict[i[0]] = i[1]
print(dict)
# #3/
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
users.sort()
list_1 = list(zip(users,num_list))
dict = {}
for i in list_1:
    dict[i[0]] = i[1]
print(dict)