# Lists are used for storing more than one value in a single variable
# e.g., Fruit list
fruit_list = ["Apple", "Guava", "Banana", "Orange"]
print(fruit_list)
print(fruit_list[0]) # this will print first fruit from the list
print(fruit_list[1]) # this will print second fruit from the list
print(fruit_list[2]) # this will print third fruit from the list
print(fruit_list[3]) # this will print fourth fruit from the list

# Using for loop for printing all elements from the fuit list
print("Printed using loop")
for fruits in fruit_list:
    print(fruits)

# Negative indexing starts from end of the list and with index (-1)
# Note: To convert negative index into positive (len(item)-(index), e.g., len(5)-2 = 3 from starting)
print("Negative indexing of the list")
print(fruit_list[-1])
print(fruit_list[-2])
print(fruit_list[-3])
print(fruit_list[-4])

# Using if-else with list
if "Apple" in fruit_list:
    print("Yes Apple is present in the List")
else:
    print("No! Apple is present in the list")

# Jump index
print(fruit_list[1:3]) # Print all list starting from 1 to 2 index
print(fruit_list[1:3:2]) # Will have gap of 2 values

# List variable
i = 0
list = [i in range(10)]
print(list)

# List comprehension - Will learn soon