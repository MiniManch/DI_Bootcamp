# Create a Door class, it has only the following attributes:
# id (int) : An id number, use a class variable objs that counts how many door have been created so far and use this number as the id of the door.
# locked (boolean)
# next (List of Door obs) : The next doors available from this one

class Door:
  num_of_doors = 0
  num_of_keys  = 2
  def __init__(self,locked,next:list = []):
    self.id = Door.num_of_doors
    self.locked = locked
    self.next = next
    Door.num_of_doors += 1
  
  # Create a method can_go_to(self, other_door) 
  # in the Door class that checks if the path from this door to other_door can be made (the locked doors cannot be opened !).
  def can_go_to(self,other_door):
    for index,door in enumerate(self.next):  
      if door.locked and Door.num_of_keys == 0:
        return False
      elif door.locked and Door.num_of_keys > 0:
        Door.num_of_keys -= 1
      if door == other_door:        
        return True
    Door.num_of_keys = 2
    
    return other_door in self.next

  def add_next_door(self,*other_doors):
    for other_door in other_doors:
      if other_door not in self.next:
        self.next.append(other_door)
    
door_1 = Door(False,[])
door_2 = Door(False,[])
door_3 = Door(True,[])
door_4 = Door(True,[])
door_5 = Door(True,[])

door_1.add_next_door(door_2,door_3,door_4,door_5)
# door_2.add_next_door(door_3,door_4,door_5)
# door_3.add_next_door(door_4,door_5)
# door_4.add_next_door(door_5)

print(door_1.can_go_to(door_5))


