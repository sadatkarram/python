
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
        parent = super().speaks()
        return f"{parent} and Woof !!"
    

dog=Dog("Buddy")
print(dog.speaks())
