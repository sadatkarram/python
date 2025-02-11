# Lambda Function : Its function with no name and keywords like def/return


#Syntax:
# lambda arguments : expression


sum = lambda x,y : x+y
print("Sum of 2 and 3 is ",sum(2,3))

square = lambda x : x**2
print("Square of 2 is ",square(2))

is_even = lambda num : "Even" if num%2 == 0 else "Odd"
print("Number 28 is ",is_even(28))
print("Number 33 is ",is_even(33))

is_positive = lambda num : "Positive" if num >=0 else "Negative"
print("Number  28 is ",is_positive(28))
print("Number -33 is ",is_positive(-33))


# Using LAMBDA in map()

numbers = [1, 2, 3, 4]
print("Original numbers list : ",numbers)
squares = list(map(lambda num : num ** 2, numbers))
print("Square of all number in list using map() :", squares)

# Using LAMBDA in filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("Original numbers list : ",numbers)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Only even number list using filter() :", even_numbers)

# Using LAMBA with Sorted()

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
print(students)
sorted_students = sorted(students, key=lambda x: x[1]) # x[1] is marks (85,92,78) arrange tuples using this mark
print("Sort student on basis of Marks")
print(sorted_students)  



# Sum of 2 and 3 is  5
# Square of 2 is  4
# Number 28 is  Even
# Number 33 is  Odd
# Number  28 is  Positive
# Number -33 is  Negative
# Original numbers list                    : [1, 2, 3, 4]
# Square of all number in list using map() : [1, 4, 9, 16]
# Original numbers list                :  [1, 2, 3, 4, 5, 6, 7, 8]
# Only even number list using filter() :  [2, 4, 6, 8]
# [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
# Sort student on basis of Marks
# [('Charlie', 78), ('Alice', 85), ('Bob', 92)]
