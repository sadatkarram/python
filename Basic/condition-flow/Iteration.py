# Iteration Example : 

print("For:  Range of numbers from 1 to 6 :")
for number in range(1,6):
    print(number)

numberList = [1, 2, 3, 4, 5]
print("For: List of numbers")
for number in numberList:
    print(number)


numberTuple = [11, 12, 13, 14, 15]
print("For: List of numbers")
for number in numberTuple:
    print(number)


## While  Example :
print("While: Print counter until it reached 5")
counter =0
while counter<5:
    print(counter)
    counter+=1 # increment by 1


 # Break and Continue

print("Break example for condition number==3")
for number in range(1,6):
    if number == 3 : 
        break
    print(number)


print("Continue example for condition number==3")
for number in range(1,6):
    if number == 3 : 
        continue
    print(number)


 ## For Loop use indentation identify its body(BLOCK)

for i in range(2):
    print("Outer Loop :",i)
    for j in range(3):
        print("Inner Loop :",j) 


# For:  Range of numbers from 1 to 6 :
# 1
# 2
# 3
# 4
# 5
# For: List of numbers
# 1
# 2
# 3
# 4
# 5
# For: List of numbers
# 11
# 12
# 13
# 14
# 15
# While: Print counter until it reached 5
# 0
# 1
# 2
# 3
# 4
# Break example
# 1
# 2
# LM0001328:test-python ram.sadatkar$ /Users/ram.sadatkar/.pyenv/versions/3.13.2/bin/python /Users/ram.sadatkar/Documents/Learning/Python/test-python/Basic/condition-flow/Iteration.py
# For:  Range of numbers from 1 to 6 :
# 1
# 2
# 3
# 4
# 5
# For: List of numbers
# 1
# 2
# 3
# 4
# 5
# For: List of numbers
# 11
# 12
# 13
# 14
# 15
# While: Print counter until it reached 5
# 0
# 1
# 2
# 3
# 4
# Break example for condition number==3
# 1
# 2
# Continue example for condition number==3
# 1
# 2
# 4
# 5
# LM0001328:test-python ram.sadatkar$ /Users/ram.sadatkar/.pyenv/versions/3.13.2/bin/python /Users/ram.sadatkar/Documents/Learning/Python/test-python/Basic/condition-flow/Iteration.py
# For:  Range of numbers from 1 to 6 :
# 1
# 2
# 3
# 4
# 5
# For: List of numbers
# 1
# 2
# 3
# 4
# 5
# For: List of numbers
# 11
# 12
# 13
# 14
# 15
# While: Print counter until it reached 5
# 0
# 1
# 2
# 3
# 4
# Break example for condition number==3
# 1
# 2
# Continue example for condition number==3
# 1
# 2
# 4
# 5
# Outer Loop
# Inner Loop
# Inner Loop
# LM0001328:test-python ram.sadatkar$ /Users/ram.sadatkar/.pyenv/versions/3.13.2/bin/python /Users/ram.sadatkar/Documents/Learning/Python/test-python/Basic/condition-flow/Iteration.py
# For:  Range of numbers from 1 to 6 :
# 1
# 2
# 3
# 4
# 5
# For: List of numbers
# 1
# 2
# 3
# 4
# 5
# For: List of numbers
# 11
# 12
# 13
# 14
# 15
# While: Print counter until it reached 5
# 0
# 1
# 2
# 3
# 4
# Break example for condition number==3
# 1
# 2
# Continue example for condition number==3
# 1
# 2
# 4
# 5
# Outer Loop
# Inner Loop
# Inner Loop
# Outer Loop
# Inner Loop
# Inner Loop
# LM0001328:test-python ram.sadatkar$ /Users/ram.sadatkar/.pyenv/versions/3.13.2/bin/python /Users/ram.sadatkar/Documents/Learning/Python/test-python/Basic/condition-flow/Iteration.py
# For:  Range of numbers from 1 to 6 :
# 1
# 2
# 3
# 4
# 5
# For: List of numbers
# 1
# 2
# 3
# 4
# 5
# For: List of numbers
# 11
# 12
# 13
# 14
# 15
# While: Print counter until it reached 5
# 0
# 1
# 2
# 3
# 4
# Break example for condition number==3
# 1
# 2
# Continue example for condition number==3
# 1
# 2
# 4
# 5
# Outer Loop : 0
# Inner Loop : 0
# Inner Loop : 1
# Inner Loop : 2
# Outer Loop : 1
# Inner Loop : 0
# Inner Loop : 1
# Inner Loop : 2
# LM0001328:test-python ram.sadatkar$ /Users/ram.sadatkar/.pyenv/versions/3.13.2/bin/python /Users/ram.sadatkar/Documents/Learning/Python/test-python/Basic/condition-flow/Iteration.py
# For:  Range of numbers from 1 to 6 :
# 1
# 2
# 3
# 4
# 5
# For: List of numbers
# 1
# 2
# 3
# 4
# 5
# For: List of numbers
# 11
# 12
# 13
# 14
# 15
# While: Print counter until it reached 5
# 0
# 1
# 2
# 3
# 4
# Break example for condition number==3
# 1
# 2
# Continue example for condition number==3
# 1
# 2
# 4
# 5
# Outer Loop : 0
# Inner Loop : 0
# Inner Loop : 1
# Inner Loop : 2
# Outer Loop : 1
# Inner Loop : 0
# Inner Loop : 1
# Inner Loop : 2
