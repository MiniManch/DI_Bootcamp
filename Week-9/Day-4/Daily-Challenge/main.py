class Person:
  def __init__(self,name):
    self.name = name
    self.hate_list = []
    self.love_list = []
    i = 0
    while True:
      if i == 2:
        break
      elif i == 0:
        user_input = input('if theres a food you LOVE, please enter it and ill add it to a list! \n enter stop to stop :) \n').lower().capitalize()
        if user_input == "Stop":
          i+=1
        else:
          self.love_list.append(user_input)
      elif i == 1:
        user_input = input('if theres a food you HATE, please enter it and ill add it to a list! \n enter stop to stop :) \n').lower().capitalize()
        if user_input == "Stop":
          i+=1
        else:
          self.hate_list.append(user_input)

  def taste(self,food_name):
    dict_to_check = {
      "love": self.love_list,
      "hate": self.hate_list
      }
    love_or_hate = [x for x, seq in dict_to_check.items() if food_name in seq]
    if len(love_or_hate) == 0:
      love_or_hate = ''
    else:
       love_or_hate = f' he {love_or_hate[0].upper()}S it!'
    
    print(f'{self.name} tastes {food_name}.{love_or_hate}')
    
      
mano = Person('mano')
mano.taste('Cucumber')
      
        
      
