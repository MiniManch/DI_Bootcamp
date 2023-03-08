# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code
from faker import Faker
fake = Faker()

class readThatText:
  def __init__(self,user_str):
    self.string = user_str

    # a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
  def frequency(self,user_word):
    freq = None
    self.stripped_str = self.string.split()
    if user_word in self.stripped_str:
      freq = 0
      for word in self.stripped_str:
        if user_word == word:
          freq += 1
    return freq

# a method that returns the most common word in the text.
  def most_common(self):
    all_freq = {}
    for word in self.stripped_str:
        if word in all_freq:
            all_freq[word] += 1
        else:
            all_freq[word] = 1
    all_freq = sorted(all_freq.items(),key = lambda x:x[1], reverse = True)
    self.all_freq = all_freq
    return all_freq[0:5]
    
# a method that returns a list of all the unique words in the text.
  def unique_words(self):
    unique_list = []
    for word_touple in self.all_freq:
      if word_touple[1] == 1:
        unique_list.append(word_touple)
    self.unique_list = unique_list
    return unique_list[0:5]
    
# Implement a classmethod that returns a Text instance but with a text file:
  @classmethod
  def from_text_file(cls,text_file):
    with open(text_file,'r+') as f:
      lines = f.readlines()
      lines = ' '.join(lines).strip('\n')
    print('1')
    return cls(lines)
    
# my_Text = readThatText(fake.text(300))
# print(my_Text.frequency('ball'))
# print(my_Text.most_common())
# print(my_Text.unique_words())

# theStranger = readThatText.from_text_file('text.txt')

# print(theStranger.frequency('ball'))
# print(theStranger.most_common())
# print(theStranger.unique_words())
import string
import gensim
from gensim.parsing.preprocessing import remove_stopwords

class textModification(readThatText):
  def __str__(self):
    return self.string[0:10]
    
  # a method that returns the text without any punctuation.
  # a method that returns the text without any special characters.

  def no_punc(self):
    self.string_no_punc = ''
    for letter in self.string:
      if letter not in string.punctuation:
        self.string_no_punc = self.string_no_punc + letter
    return self.string_no_punc[0:200]

  # a method that returns the text without any english stop-words
  def no_stop(self):
    self.string_no_stop = remove_stopwords(self.string)
    return(self.string_no_stop[0:200])
    
modi = textModification.from_text_file('text.txt')
print(modi.no_punc())
print('stop \n',modi.no_stop())


