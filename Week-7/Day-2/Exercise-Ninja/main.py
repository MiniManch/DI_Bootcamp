# Exercise Ninja
# Challenge 1
# Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
def string_in_stars():
  user_input = input('Give me a string please \n')
  input_list = user_input.split()
  longest = ''
  for word in input_list:
    if len(word) > len(longest):
      longest = word
  max_length = len(longest)
  print(longest)
  print('*' * (max_length + 4))
  for word in input_list:
    word_len = len(word)
    spaces_list = []
    for x in range(0,max_length - word_len):
      spaces_list.append(' ')
    spaces = ''.join(spaces_list)
    print('* ' + word + spaces + " *")
  print('*' * (max_length + 4))

string_in_stars()

# Challenge 2
def insertion_sort(alist):
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     # shouldve used enumerate

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
# perhaps find highest value in list?
alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)
