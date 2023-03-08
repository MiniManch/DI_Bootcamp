import random

def get_words_from_file(file_name):
  with open(file_name,'r+') as f:
    lines = f.readlines()
    lines = ''.join(lines).split()
  return lines

def get_random_sentence(length:int):
  random_Sentence = ''
  lines = get_words_from_file('text.txt')
  for x in range(0,length):
    if x == 0:
      random_Sentence =  lines[random.randint(0,(len(lines)-1))].capitalize()
    else:
      random_Sentence = random_Sentence + ' ' + lines[random.randint(0,(len(lines)-1))].capitalize()
  return random_Sentence

# print(get_random_sentence(7))
def main():
  user_length = input('Please enter the length of the sentence that you want. \n it can be 2-20.\n')
  if not user_length.isnumeric():
    raise TypeError("Only integers are allowed")
  user_length = int(user_length)
  if user_length > 20 or user_length < 2:
    raise ValueError('Value can be between 2-20 try again.')
  return get_random_sentence(user_length)
  
print(main())

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_in_json = json.loads(sampleJson)
# Access the nested “salary” key from the JSON-string.
salary = json_in_json['company']['employee']['payable']['salary']
# print(salary)

# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
json_in_json['company']['employee']['birth_date'] = '1996/05/02'
# print(json_in_json)

 # Save the dictionary as JSON to a file.

json_object = json.dumps(json_in_json, indent=4)
with open("solution.json", "w") as f:
    f.write(json_object)

