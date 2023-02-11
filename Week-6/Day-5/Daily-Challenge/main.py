# Daily Challenge 1
user_string = input('give me a string please \n')
while not user_string.isalpha():
  user_string = input(
    'yes but this time dont enter a number or a symbol just letters\n')
letter_dict = {}
for index, letter in enumerate(user_string):
  # check if key already exists, if it doesnt, add key and value of index in array
  # if it does exist, add the index into the value arrray
  if letter not in letter_dict.keys():
    letter_dict[letter] = [index]
  else:
    letter_dict[letter].append(index)

print(letter_dict)

# Daily Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.

wallet = input('How much do you have in your wallet mister? \n')
while not wallet.isnumeric():
  wallet = input(
    'try again, this time only give me an input of numbers please \n')

store_items = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20",
  "Phone": '$100,000,000',
  'Yacht': '$70'
}
items_you_can_buy = []
for elem in store_items:
  elem_int = int(store_items[elem].replace('$', '').replace(',', ''))
  if elem_int <= int(wallet):
    print(
      f"you can afford to get yourself a {elem} for the price of {store_items[elem]}"
    )
    items_you_can_buy.append(elem)

if len(items_you_can_buy) == 0:
  print('You cant afford anything sorry')
else:
  print(items_you_can_buy)
