
## Polymorphism with Abstract Classes : We can enforce method overriding using abstract classes.
print("Example: Using ABC (Abstract Base Class)")

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof !!"

class Cat(Animal):
    def speak(self):
        return "MeoW !!"
    
animals = [Dog(), Cat()]
for animal in animals :
    print(animal.speak())


# Example: Using ABC (Abstract Base Class)
# Woof !!
# MeoW !!