from datetime import datetime, date, timedelta
import Airline
import Airport
import Airplane
import Flight



flight_list = [{
  'destination': 'Nicaragua',
  'date': datetime(2023, 8, 15)
}, {
  'destination': 'Belgium',
  'date': datetime(2023, 7, 18)
}, {
  'destination': 'Paris',
  'date': datetime(2023, 2, 11)
}]

G86 = Airplane.Airplane('Wizz1', 'Guatamala', '', flight_list)
WizzAir = Airline.Airline('1111', 'Wizz Air', [G86])

G86.add_Airline(WizzAir)
my_flight = Flight.Flight('Nicaragua','Belgium',G86,datetime(2023, 8, 15))

Paris_Central = Airport.Airport('Paris_1',[G86],[],[{
  'destination': 'Paris',
  'date': datetime(2023, 2, 11)
}])

# print(my_flight)
print(G86)
print(WizzAir)

print(G86.location_on_date(datetime(2023,7,18)))
print(G86.available_on_date(datetime(2023,7,18),'Belgium'))
print(G86.available_on_date(datetime(2023,2,18),'Belgium'))

Paris_Central.schedule_flight('Belgium',datetime(2023,7,18))
print(Paris_Central)