
# Polymorphism means "many forms." 
# It allows different classes to have methods with the same name, but different behaviors

# Different classes can have the same method name, but behave differently.
# Example: speak() Method in Different Classes

class Dog:
    def speak():
        print("Woof !!")
class Cat:
    def speak():
        print("Meow !!")
class Cow:
    def speak():
        print("Moo !!")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()