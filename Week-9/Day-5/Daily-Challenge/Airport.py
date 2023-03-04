import Airline
import Airplane
import Flight
from datetime import datetime, date, timedelta


class Airport:
  def __init__(self,city_id:str,planes:list,scheduled_departures:list = [] ,scheduled_arrivals:list = []):
    self.city_id = city_id
    self.planes  = planes
    self.scheduled_departures = scheduled_departures
    self.scheduled_departures.sort(key= lambda x: x['date'])
    
    self.scheduled_arrivals   = scheduled_arrivals
    self.scheduled_arrivals.sort(key= lambda x: x['date'])
    
  def __str__(self):
    return f'{self.city_id}:city \n {self.planes}:planes \n {self.scheduled_departures}:departures \n {self.scheduled_arrivals}:arrivals'
    
  def schedule_flight(self,destination,date_from_user):
    for plane in self.planes:
      if plane.available_on_date(date_from_user,destination):
        flight = {'destination':destination,'date':date_from_user}
        plane.next_flights.append(flight)
        plane.next_flights.sort(key=lambda x: x['date'])
        self.scheduled_departures.append(flight)
        print('yay')
        return True
    print('nay')
    return False

    