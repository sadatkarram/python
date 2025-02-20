
## Encapsulation in Python

# Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP).
# It refers to restricting direct access to certain details of an object 
# and only exposing necessary parts.


class Car :
    def __init__(self, brand, speed) :
        self.brand = brand
        self.speed = speed

car  = Car("Toyota", 200)
print("Car Brand :",car.brand)
print("Car Speed :",car.speed)

car.speed = 250
print("New Speed of Car :",car.speed)

# Car Brand : Toyota
# Car Speed : 200
# New Speed of Car : 250



## Protected Attributes (Convention: _name)
# In Python, protected attributes are not strictly enforced but should be treated as internal.

class Car :
    def __init__(self, brand, speed) :
        self._brand = brand
        self._speed = speed

car  = Car("Toyota", 200)
print("Car Brand :",car._brand)
print("Car Speed :",car._speed)

# Although accessible, protected attributes should not be modified directly outside the class.



##Private Attributes (Not Directly Accessible)
 # Private attributes cannot be accessed directly from outside the class.
# Using Getter & Setter Methods : To access and modify private attributes, we use getter and setter methods.
# Example: Encapsulation with Getters & Setters


class BankAccount :
    def __init__(self, __balance):
        self.__balance = __balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance >= 0 :
            self.__balance = balance
        else :
            print("Invalid input")


bk_account = BankAccount(1000)
print("Bank Account balance : ",bk_account.get_balance())

bk_account.set_balance(bk_account.get_balance()+1000)
print("Post deposite of 1000 Rs, account balance is : ",bk_account.get_balance())

bk_account.set_balance(-500)

# Bank Account balance :  1000
# Post deposite of 1000 Rs, account balance is :  2000
# Invalid input




## Using @property for Encapsulation
# Example: Using @property

class Employee :
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self.salary 
    
    @salary.setter
    def salary(self, amount):
        if amount > 0 :
            self.salary = amount
        else :
            print("Salary must be positive")
    

emp = Employee("Ram",10000)
print("Employee name :",emp.name)
print("Before Change : Employee salary :",emp.salary)
emp.salary = 50000
print("After Change  : Employee salary :",emp.salary)
emp.salary=-100




        
