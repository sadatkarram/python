
# Overloading and Overriding example


# Method Overloading (Same Method, Different Parameters)
# Example: Method Overloading with Default Arguments

class MathOpertion :
    def add (self, a , b=0, c=0):
        return a+b+c
    

sum = MathOpertion()
print(sum.add(1))
print(sum.add(1, 2))
print(sum.add(1, 2, 3))
print(sum.add(1, 2, 4))

# 1
# 3
# 6
# 7

# Method Overriding (Child Replaces Parent Method)
# Example: Method Overriding in Python

class Parent :
    def greeting(self) :
        print("Hello from Parent Class")

class Child(Parent) :
    def greeting(self) :
        print("Hello from Child Class")

test = Child()
print(test.greeting())
print("End")

# Hello from Child Class
# None
# End


# Calling Parent Method in Overriding

class Parent :
    def greeting(self) :
        return "This is the Parent class"

class Child(Parent) :
    def greeting(self) :
        parent_message = super().greeting()
        return f"{parent_message}"

# Creating an object
obj = Child()
print(obj.greeting())
# The child method extends the parent method instead of fully replacing it.