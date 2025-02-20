class Person :
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_details(self):
        return f"Person name is {self.name}, age is {self.age}"

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade=grade

    def get_details(self):
        parent = super().get_details()
        return f"{parent} and his grade is {self.grade}"

student = Student("Ram",33, "A")
print(student.get_details())
