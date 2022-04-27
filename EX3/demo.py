# Create one class called FruitShop. This class should receive a name which should be a string, and fruits as a list. 
# Create also a method called get_fruits_count() which should return amount of fruits in the shop.
# Input:
# my_shop = FruitShop("My Fruit Shop", ["Banana" , "Orange", "Kiwi", "Apple"])
# Output: 4
 
#  .....................................................................
#  ////My Solution///
fruit=[]
class FruitShop():

      def __init__(self,name,fruit):      
           self.name = name
           self.fruit=fruit
          
      def get_fruits_count(self):
        count=len(self.fruit)
        print(count)
          
# my_shop = FruitShop("My Fruit Shop", ["Banana" , "Orange", "Kiwi", "Apple"])
# my_shop.get_fruits_count()

# LAB 2 - OOP



# Create the following classes: Animal, Horse and Dog.
# The Animal class should have a method eat ( ) and it should return "eating.. nom.. nom.."
# The Horse class should have a method called neigh ( ) and it should return "neigh! "
# The Dog class should have a method called bark ( ) and it should return "voof voof!"
# And remember that the Horse and Dog class should inherit form the Animal class.

class Animal():
   def __init__(self) :
     print("Animal Created")
     
   def eat(self):
      print("eating ...nom..nom")   
 
class Horse(Animal):
    def __init__(self):
     Animal.__init__(self)
    print("Horse Created")
     
    def neigh(self):
      print("Neighhhh")
class Dog(Animal):
   def __init(self):
     Animal.__init__(self)
     print("Dog created")
      
   def bark(self):
    print("voof voof ")        
   
d=Dog()
d.eat()
d.bark()

#  LAB 3 - OOP


# Create the following classes: 
# Person
# Staff
# Busdriver
# Person should have one method named walk( ) that should return "walking"
# Staff should have one method called work( ) that should return "working"
# Busdriver should have one method called driving ( ) that returns "diving the bus"
# The Busdriver class should inherit from both Person and Staff 

class Person():
    def __init__(self):
     print("person Created")
    
    def walk(self):
     print("walking")
     
     
class Staff(Person):
  def __init__(self):
      Person.__init__(self)
      print("staff created")
    
  def work(self):
    print("working")  
class driver(Staff):
  def __init__(self):
       Staff.__init__(self)
  def drive(self):
   print("Driving the bus")    
d=driver()
d.work()
d.walk()