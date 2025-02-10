
# List Example

fruits = ["Apple", "Orange", "Mango"]
print("Before :",fruits)

fruits[0]="PineApple"
print("After :",fruits)

fruits.append("grape")
print("After-append :",fruits)

fruits.remove("Orange")
print("After-remove :",fruits)

print("Index of PineApple :",fruits.index("PineApple"))


""" 📌 Common List Methods

Method	    Description	                            Example
=============================================================
append()	Adds an element to the end	            list.append(4)
extend()	Adds multiple elements	                list.extend([5, 6])
insert()	Inserts at a specific index	            list.insert(1, "Hello")
remove()	Removes the first occurrence of a value	list.remove(3)
pop()	    Removes and returns an element	        list.pop(2)
index() 	Returns the index of a value	        list.index(2)
count()	    Counts occurrences of a value	        list.count(3)
sort()	    Sorts the list in ascending order	    list.sort()
reverse()	Reverses the list order	                list.reverse()
copy()	    Returns a copy of the list	            new_list = list.copy()
clear()	    Removes all elements	                list.clear()

 """

