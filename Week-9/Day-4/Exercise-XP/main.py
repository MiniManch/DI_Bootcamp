# Create a class Human, it has the following attributes:
# name (str)
# age (int)
# living_place (Building - Default is None)
class Human:

  def __init__(self, name, age, living_place=None):
    self.name = name
    self.age = age
    self.living_place = living_place

    # Add the move(self, building) method to the Human class,
    # it sets the living place of this human to the building and add this human to the building inhabitants.

  def move(self, building):
    self.living_place = building
    building.inhabitants.append(self)
    print(f'{self.name} moved to {self.living_place.address}')


# create another class Building, it has the following attributes:
# address (str)
# inhabitants (List of Human objects - Default is empty)
class Building:
  num_of_inhabitants = 0

  def __init__(self, address: str, inhabitants: list):
    self.address = address
    self.inhabitants = inhabitants
    Building.num_of_inhabitants += len(self.inhabitants)


# Create a class City, it has the following attributes:
# name (str)
# buildings (List of Building objects - Default is empty)
class City:

  def __init__(self, name: str, buildings: list):
    self.name = name
    self.buildings = buildings

  # Add the construct(self, address) method to the City class, it adds a building at the referenced address.
  def construct(self, address, inhabitants):
    new_building = Building(address, inhabitants)
    self.buildings.append(new_building)
    return new_building

  # Add the info(self, address) method to the City class, it displays the number of buildings and the mean age of the citizens.

  def info(self, address):
    for building in self.buildings:
      if address == building.address:
        selected_building = building

    age_list = []
    for resident in selected_building.inhabitants:
      age_list.append(resident.age)

    mean_of_ages = sum(age_list) / len(age_list)
    return f'the building on {selected_building.address} has inhabitants with the average age of {mean_of_ages}'
