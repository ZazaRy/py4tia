#Lists! One of the most versatile data types in Python. Lists are used to store multiple items in a single variable. Lists are created using square brackets.

mylist = ["Storm", "The Legendary Blue Fish", "The Storminator"]
print(mylist)

#Like strings ( because strings are actually arrays ) lists are indexed.
print(f"print(mylist[0]) = {mylist[0]}")
print(f"print(mylist[1]) = {mylist[1]}")
print(f"print(mylist[2]) = {mylist[2]}")

#Both strings and lists can be iterated over.
for item in mylist:
    print(item)

for item in mylist:
    for letter in item:
        print(letter)


#List comprehension is a way to create lists in Python. It is a compact way to create lists.
#Syntax: newlist = [expression for item in iterable if condition == True]

#Example
newlist = [x for x in range(10)]
print(newlist)
#Here we did not need a condition, so we left it out.

#If we wanted to create a list of only the even numbers from 0 to 9, we could do this:
newlist = [x for x in range(10) if x % 2 == 0]
print(newlist)
for i in mylist:
    for j in i:
        print(j)
