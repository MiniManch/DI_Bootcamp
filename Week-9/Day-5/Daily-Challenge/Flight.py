import Airline
import Airport
import Airplane
from datetime import datetime, date, timedelta


class Flight:
  def __init__(self,destination,origin,plane,date_from_user):
    self.destination = destination
    self.origin      = origin
    self.plane       = plane
    self.date        = date_from_user
    self.id          = f'{date_from_user.month}-{date_from_user.day}-{destination}-{self.plane.airline.id}-{self.plane.airline.name}'

  def take_off(self):
    self.plane.current_location = 'in air'

  def land(self):
    self.plane.current_location = self.destination
