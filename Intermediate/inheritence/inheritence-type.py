
#
# Types of Inheritance
# Python supports multiple types of inheritance:

# Type	                    Description
# Single Inheritance	    One child class inherits from one parent class
# Multiple Inheritance	    A child class inherits from multiple parent classes
# Multilevel Inheritance	A child class inherits from another child class
# Hierarchical Inheritance	Multiple child classes inherit from one parent class
# Hybrid Inheritance	    Combination of different inheritance types


## Single Inheritance (Basic)
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Animal sound"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Creating an object of Dog
dog = Dog("Buddy")
print(dog.name)       # ✅ Output: Buddy
print(dog.speak())    # ✅ Output: Woof!


# Calling Parent Methods with super()
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return super().speak() + " and Woof!"

# Creating an object
dog = Dog()
print(dog.speak())  # ✅ Output: Animal sound and Woof!




## Multiple Inheritance
class Engine:
    def start(self):
        return "Engine started"

class Wheels:
    def roll(self):
        return "Wheels rolling"

class Car(Engine, Wheels):  # Inheriting from both classes
    def drive(self):
        return "Car is moving"

# Creating object
car = Car()
print(car.start())  # ✅ Output: Engine started
print(car.roll())   # ✅ Output: Wheels rolling
print(car.drive())  # ✅ Output: Car is moving



## Multilevel Inheritance
#A child class inherits from another child class (parent → child → grandchild).
class Animal:
    def move(self):
        return "Animals can move"

class Mammal(Animal):
    def has_fur(self):
        return "Mammals have fur"

class Dog(Mammal):
    def speak(self):
        return "Woof!"

# Creating object
dog = Dog()
print(dog.move())   # ✅ Output: Animals can move
print(dog.has_fur())  # ✅ Output: Mammals have fur
print(dog.speak())   # ✅ Output: Woof!



##Hierarchical Inheritance
#One parent class has multiple child classes.

class Animal:
    def move(self):
        return "Animals move"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating objects
dog = Dog()
cat = Cat()

print(dog.move())   # ✅ Output: Animals move
print(dog.speak())  # ✅ Output: Woof!
print(cat.move())   # ✅ Output: Animals move
print(cat.speak())  # ✅ Output: Meow!



### Method Resolution Order (MRO)
# When a child class inherits from multiple parents, Python follows MRO (left-to-right) to determine which method to call.
class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"

class C(A):
    def show(self):
        return "C"

class D(B, C):  # Inheriting from B and C
    pass

# Creating object
d = D()
print(d.show())  # ✅ Output: B (Because B is inherited first)


