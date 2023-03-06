# ran pip instgall translate in shell

from translate import Translator
Eng_trans = Translator(from_lang = 'fr',to_lang='en')

translated_dict = {}
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

for word in french_words:
  translated_dict[word] = Eng_trans.translate(word)

print(translated_dict)