
# Inheritence: Child class has access to method and attribute to use it freely as its own.


#Parent class
class Animal :
    def __init__(self, name) :
        self.name = name
    
    def speaks(self) :
        return "Animal Sound !!"
    

#Child Class
class Dog(Animal) :
    def __init__(self,name):
        super().__init__(name)
        self.name=name


    def speaks(self):
        return "Woof !"
    

dog=Dog("Buddy")
print(f"{dog.name} says {dog.speaks()}")
print(f"{dog.name} says {super.self.speaks()}")