
# Class 


class Car :
    def __init__(self, brand, model) :
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car :{self.brand} {self.model}")

car1 = Car("Toyota","Corolla")
car1.display_info()