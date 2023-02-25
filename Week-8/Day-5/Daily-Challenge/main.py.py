# OOP QUIZ
# Q What is a class?
# A class is a defined object type, with our own unique defined characteristics and methods

# Q What is an instance?
# A an instance is an object of a certain class.

# Q What is encapsulation?
# A Encapsulation allows you to hide specific information and control access to the internal state of the object.

# Q What is abstraction?
# A simplyfying functions, forinstance if we have a coffee machine, the user clicks on coffee or whatever, and is not aware that the machine is crushing the coffee, then boils the water, the combines, then filters and so on and so on.

# Q What is inheritance?
# A basicaly inherting methods ands characteristics of a father class, for instance, every dog is an animal, but not all animals are dogs, so dogs should have the characteristics of an animal but not all animals have the characteristics of a dog.

# Q What is multiple inheritance?
# A basically like inheritance but multiple? for example a dog can be an animal a mammal . or dog and brown. whatever.

# Q What is polymorphism?
# A making our classes inherite different  methods that act differently depeding on the child we call it. for instance the  + operator acts differently if its adding up numbers or when its adding up strins and such. same way we can program our classes and methods inside them

# Q What is method resolution order or MRO?
# A Basically that if we have lets say Cat(Animal,lazy) ,which each of the classes hold the makesound method, we will first check if Cat class has it, then if animal,then if lazy. 

# making a deck of cards
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
import random

suit_list = ['Hearts','Diamonds','Clubs','Spades']
class Cards:
  def __init__(self,suit):
      while suit not in suit_list:
        suit = input('please choose Heart,Diamonds,Clubs or Spades').lower().capitalize()
      self.suit  = suit
      self.cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

class Deck:
  def __init__(self,Cards_l):
    self.cards = []
    for cards in Cards_l:
      i = 0
      for card in cards.cards:
        self.cards.append({cards.suit:card})
    print(self.cards)

  def shuffle_deck(self):
    print(self.cards)
    random.shuffle(self.cards)
    print(self.cards)
    return self

  def deal(self):
    dealt_card = random.choice(self.cards)
    self.cards.remove(dealt_card)
    return dealt_card

cards_1 = Cards('Hearts')
cards_2 = Cards('Diamonds')
cards_3 = Cards('Clubs')
cards_4 = Cards('Spades')

cards_list = [cards_1,cards_2,cards_3,cards_4]
deck = Deck(cards_list)

deck.shuffle_deck()
[print(deck.deal())
        
        