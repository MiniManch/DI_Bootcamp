# Exercise 1
class Trial_class:
  def __init__(self,value):
    self.value = value
    

  def __abs__(self):
    return abs(self.value)
    
  def __int__(self):
    if int(self.value):
      return True
    return False
    
  # def __input__(self,value)
  @staticmethod
  def __doc__():
    print('this class has special int() and abs() functions, which return data as such as: ')
    print('abs will return the absolute value of the object')
    print('int will return bool defining wether the value is int or not')
    
    
x = Trial_class(-5)
print(abs(x),'abs')
Trial_class.__doc__()

#  Didnt understand how to do that with input(), couldnt find dunder of it

# Exercise 2
class Currency:

  def __init__(self, currency, amount):
    self.currency = currency
    self.amount = amount

    #Your code starts HERE
# print + repr

  def __repr__(self):
    return f'{self.amount} {self.currency}'

# int

  def __int__(self):
    return int(self.amount)


# +

  def __add__(self, other):
    if type(other) == int:
      return self.amount + other
    elif type(other) == type(self):
      if self.currency != other.currency:
        raise Exception('Cannot add up different currencies')
      else:
        return self.amount + other.amount

  # +=
  def __iadd__(self, other):
    if type(other) == int:
      self.amount += other
    elif type(other) == type(self):
      if self.currency != other.currency:
        raise Exception('Cannot add up different currencies')
      else:
        self.amount + other.amount

Cur_1 = Currency('dollar', 5)
Cur_2 = Currency('yaa', 20)
Cur_3 = Currency('dollar', 10)

print(Cur_1 + 6)
print(Cur_1 + Cur_3)
print(Cur_1 + Cur_2)
