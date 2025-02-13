
class Person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def greeting(self) :
        print("Hello",self.name, "!!")
    
    def askAge(self) :
        print("My age",self.age,"years")

ram = Person("Ram", 33)
ram.greeting()
ram.askAge()

# Hello Ram !!
# My age 33 years