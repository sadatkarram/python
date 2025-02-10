# Tuple Example

numbers=(1,2,2,3,4,5,3,2,3,3,3)

print("Before :",numbers)

print("Min :",min(numbers))
print("Max :",max(numbers))
print("Sorted :",sorted(numbers))
print("Count 2 :",numbers.count(2))
print("Count 3 :",numbers.count(3))

# Before : (1, 2, 2, 3, 4, 5, 3, 2, 3, 3, 3)
# Min : 1
# Max : 5
# Sorted : [1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5]
# Count 2 : 3
# Count 3 : 5
