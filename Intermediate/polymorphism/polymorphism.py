
# Polymorphism means "many forms." 
# It allows different classes to have methods with the same name, but different behaviors

# Different classes can have the same method name, but behave differently.
print("Example: speak() Method in Different Classes")

class Dog:
    def speak(slef):
        print("Woof !!")

class Cat:
    def speak(self):
        print("Meow !!")

class Cow:
    def speak(self):
        print("Moo !!")
        

animals = [Dog(), Cat(), Cow()]

for animal in animals :
    animal.speak()

#Example: speak() Method in Different Classes
# Woof !!
# Meow !!
# Moo !!

## Polymorphism in Inheritance
print("Example: Overriding Parent Method")

class Bird:
    def fly(self):
        print("Some bird can fly")

class Pigeon(Bird):
    def fly(self):
        print("Pigeon can fly !!")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly **")

birds = [Bird(), Pigeon(), Penguin()]
for bird in birds:
    bird.fly()

# Example: Overriding Parent Method
# Some bird can fly
# Pigeon can fly !!
# Penguin cannot fly **


## Polymorphism with Functions : A single function can work with different types of objects.
print("Example: Function Working with Different Objects")

def animal_sound(animal):
    animal.speak()

animal_sound(Dog())
animal_sound(Cat())
animal_sound(Cow())

# Example: Function Working with Different Objects
# Woof !!
# Meow !!
# Moo !!

## Polymorphism with Abstract Classes
print("Example: Using ABC (Abstract Base Class)")