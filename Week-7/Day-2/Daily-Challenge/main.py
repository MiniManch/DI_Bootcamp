# Matrix Challenge
given_string = '''7i3
                  Tsi
                  h%x
                  i #
                  sM 
                  $a 
                  #t%
                  ^r!
              '''

split_given_string = given_string.replace(' ', '').split('\n')
# using ''' string, so i fiddle with some spacing and i received a vacant
# string as the last item of the array. so removed that
split_given_string.pop(-1)
first_letter_list = []
second_letter_list = []
third_letter_list = []
for index, item in enumerate(split_given_string):
  if len(item) == 2:
    item = item + ' '
  first_letter_list.append(item[0])
  second_letter_list.append(item[1])
  third_letter_list.append(item[2])

full_letter_list = []


def add_all_items_of_list(list, list2):
  for item in list2:
    list.append(item)

add_all_items_of_list(full_letter_list, first_letter_list)
add_all_items_of_list(full_letter_list, second_letter_list)
add_all_items_of_list(full_letter_list, third_letter_list)

def no_nums_two_symbols_is_space(list):
  final_list = []
  for index, item in enumerate(list):
    if item.isalpha():
      final_list.append(item)
    elif index+1 < len(list) and not item.isalpha() and not list[index+1].isalpha():
      final_list.append(' ')
  for index,item in enumerate(final_list):
    if index+1 < len(list) and item == ' ' and final_list[index+1] == ' ':
      final_list.pop(index)
  return final_list

print(no_nums_two_symbols_is_space(full_letter_list))
