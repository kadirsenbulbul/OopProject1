class Animal():
  def __init__(self,name,age,color,teeth):
    self.name = name
    self.age = age
    self.color = color
    self.teeth = teeth

myAnimal = Animal("Flap",7,"brown",32)
print(myAnimal.name)   #Checking some properties of the class Animal
print(myAnimal.age)


class Dog(Animal):
  year = 7
  def __init__(self,name,age):
    self.__name = name
    self.age = age
    print("The dog is here.")

  def changeName(self,name):
    self.__name = name

  def humanAge(self):
    return self.age * Dog.year  #Calculates the age of the dog in human age
  def getName(self):   #we use get instead of print because we used encapsulation
    return self.__name


dogMustard = Dog("Mustard",10)
print(dogMustard.humanAge())
print(dogMustard.getName())

dogMustard.changeName("Hardal")
print(dogMustard.getName())


class Cat(Animal):
  def __init__(self,name,age,color,teeth,eyeColor):
    self.eyeColor = eyeColor
    self.__name = name
    print("I am a cat and you can't change my name.")
  def getName(self):
    return self.__name

  def changeName(self,name):
    self.__name = name

kedi = Cat("Pamuk",3,"white",30,"green")
print(kedi.getName())
print(kedi.eyeColor)

class Bird(Animal):
  def __init__(self, name, age, color, teeth):
    super().__init__(name, age, color, teeth)
    self.name = name
    self.age = age
    self.color = color
    self.teeth = teeth

  def sound (self):
    return "chirp"

boncuk = Bird("boncuk",1,"blue",2)
sukru = Bird("sukru",2,"yellow",2)

print(sukru.name)
print(boncuk.name)

bird_list = [boncuk,sukru]

for x in bird_list: # x is just a variable
  print(x.sound())

###
from abc import ABC, abstractmethod   #Abstraction
class AbcAnimal:
  @abstractmethod
  def venomous(self):
    pass

class Snake(AbcAnimal):
  def venomous(self):
    print("This is a venomous snake")

Mamba = Snake()
Mamba.venomous()
