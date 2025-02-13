
#Exception Handling 


# Single Exception handling 
try :
    result = 10 / 0
except ZeroDivisionError :
    print("Error : Cannot divide by Zero!") 

# Error : Cannot divide by Zero!


# Multiple Exception handling
try :
    num = int(input("Enter a numnber : "))
    result = 10/num
except ZeroDivisionError :
    print("Error : Cannot divide by Zero!")
except ValueError :
    print("Error : Invalid input ! Please enter a number")

# Case 1: 
# Enter a numnber : 0
# Error : Cannot divide by Zero!

# Case 2 :
# Enter a numnber : ram
# Error : Invalid input ! Please enter a number

# finally Exception handling
try :
    num = int(input("Enter a numnber : "))
    result = 10/num
except ZeroDivisionError :
    print("Error : Cannot divide by Zero!")
except ValueError :
    print("Error : Invalid input ! Please enter a number")
finally :
    print("Finally block is executed : Execution complete !!")


# Enter a numnber : 3
# Finally block is executed : Execution complete !!


# Custom Exception : raise 
print("Custom Exception : use keyword 'raise' ")
def check_age(age) :
    if age < 18:
        raise ValueError("You must be 18 or older to proceed")
    print("Access Granted")

try :
    check_age(16)
except ValueError as e :
    print("Error: ",e)

# Custom Exception : use keyword 'raise' 
# Error:  You must be 18 or older to proceed  
    
