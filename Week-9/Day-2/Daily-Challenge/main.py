import math

class Circle:
  
  def __init__(self, radius_or_diameter: dict):
    keys = list(radius_or_diameter.keys())
    if 'radius' in keys and 'diameter' not in keys:
      self.radius = radius_or_diameter['radius']
      self.diameter = self.radius * 2
      print(self.radius,self.diameter)
      
    elif 'radius' not in keys and 'diameter' in keys:
      self.diameter = radius_or_diameter['diameter']
      self.radius = self.diameter / 2
      print(self.radius,self.diameter)
      
    else:
      self.diameter = radius_or_diameter['diameter']
      self.radius = radius_or_diameter['radius']

  def calc_Area(self):
    self.area = round(math.pi * pow(self.radius,2),2)
    return self.area

  def calc_Circumfrence(self):
    self.circumfrence = round(self.radius * 2 * math.pi,2)
    return self.circumfrence
    
  def __str__(self):
    area         = self.calc_Area()
    circumfrence = self.calc_Circumfrence()
    string = f'This circle has a radius of {self.radius} therfore the diameter is {self.diameter} and the circumfrence of it is {circumfrence}. \n obviously, its area is {area}'
    return string

  def __add__(self,other):
    new_radius = {'radius':(self.radius + other.radius)}
    new_circle = Circle.create_circle(new_radius)
    return new_circle

  def __gt__(self, other):
    if self.radius > other.radius:
      return True
    return False

  def __eq__(self, other):
    if self.radius == other.radius:
      return True
    return False
    
  def __comp__(self, other):
    if self.radius == other.radius:
      return 0
    elif self.radius > other.radius:
      return 1
    elif self.radius < other.radius:
      return -1

  @classmethod
  def create_circle(cls, radius_or_diameter: dict):
    return cls(radius_or_diameter)
    


radius_Dict = {'radius': 5}
diameter_Dict = {'diameter': 6}

my_circle = Circle.create_circle(radius_Dict)
my_circle2 = Circle.create_circle(diameter_Dict)

print(my_circle)
new_circle = my_circle + my_circle2
print(my_circle == my_circle )

circle_list = [my_circle,new_circle,my_circle2]
print(circle_list)
circle_list.sort()
print(circle_list)

