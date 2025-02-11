
#Function Syntax


#Function without Parameter
def sayHello():
    print("Function without Parameter")
    print("Hello World !!")

sayHello()

# Function with Parameter
def sayHello(name):
    print("Function with Parameter")
    print("Hello :",name)

sayHello("Ram")

# Function with Return value
def add(a, b):
    return (a+b)


result = add(2,3)
print("Function with Return value")
print("Sum of 2 and 3 :",result)


#Function with default value
def greet(name="Guest") :
    print(" Hello : ",name)

print("Function with default value")
greet()
greet("Ram")
