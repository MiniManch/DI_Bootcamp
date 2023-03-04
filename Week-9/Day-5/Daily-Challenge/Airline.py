import Airport
import Airplane
import Flight
from datetime import datetime, date, timedelta



class Airline:
  def __init__(self, id: str, name: str, planes: list = []):
    self.id = id
    self.name = name
    self.planes = planes

  def __str__(self):
    return f'{self.name}:name \n {self.id}:id \n {self.planes}:planes'

