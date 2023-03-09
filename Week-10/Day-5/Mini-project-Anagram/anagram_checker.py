# pip install PyDictionary
import itertools
from spellchecker import SpellChecker

spell = SpellChecker()

class AnagramChecker:
  def __init__(self,text_file):
    self.file = text_file
    
  @staticmethod
  def is_valid_word(word):
    return word in spell #when word isnt valid returns None
    
  @staticmethod
  def get_anagrams(word):
    #check all combinations of the string if is vlaid word append to a list of anagrams
    anagram_list = []
    for perm in list(itertools.permutations(word)):
      perm = ''.join(perm)
      if AnagramChecker.is_valid_word(perm) and perm != word:
        anagram_list.append(perm)
    return anagram_list
  
my_checker = AnagramChecker('sowpods.txt')
# print(AnagramChecker.get_anagrams('team'))
# print(AnagramChecker.is_valid_word('HeLlo'))

