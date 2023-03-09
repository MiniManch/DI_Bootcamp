import anagram_checker as a_c

def menu():
  while True:
    user_input = input('Please enter a word:\n (x) to exit \n').strip(' ')
    if user_input == 'x':
      return False
    if len(user_input.split(' ')) > 1:
      raise ValueError('Only enter one word please')
    if user_input.isalpha():
      break
  return user_input

def main():
  user_word = menu()
  if not user_word:
    return 'User decided to break'
  is_valid = a_c.AnagramChecker.is_valid_word(user_word)
  if is_valid :
    is_or_not = 'is'
  else:
    is_or_not = 'is not'
  user_anagrams = a_c.AnagramChecker.get_anagrams(user_word)
  if len(user_anagrams) > 0:
    anagram_string = ','.join(user_anagrams)
  else:
    anagram_string = 'this word has no anagrams'

  final_string = f'''
                 YOUR WORD: "{user_word.upper()}"
                 this {is_or_not} a valid English word.
                 Anagrams for your word: {anagram_string}
                 '''
  return final_string
  
  
  
  
print(main())