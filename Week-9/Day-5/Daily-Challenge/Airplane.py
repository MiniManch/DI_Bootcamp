import Airport
import Flight
import Airline
from datetime import datetime, date, timedelta



class Airplane:
  def __init__(self, id, current_location, airline, next_flights: list = []):
    self.id = id
    self.current_location = current_location
    self.airline = airline
    self.next_flights = next_flights
    self.next_flights.sort(key=lambda x: x['date'])

  def fly(self, destination):
    print(
      f'Plane {self.id} will fly from {self.current_location} to {destination}'
    )
    self.current_location = destination

  def location_on_date(self, date_from_user):
    for item in self.next_flights:
      if item['date'] == date_from_user:
        return item['destination']
    return False

  def add_Airline(self, airline_Company: Airline):
    self.airline = airline_Company

  def __str__(self):
    return f'{self.current_location}:location \n {self.id}:id \n {self.airline.name}:airline \n' 
    
  def available_on_date(self, date_from_user, location):
    return self.location_on_date(date_from_user) == location
      
