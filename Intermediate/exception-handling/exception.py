
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

# Enter a numnber : 0
# Error : Cannot divide by Zero!

# Enter a numnber : ram
# Error : Invalid input ! Please enter a number
