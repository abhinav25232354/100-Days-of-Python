# Use of for loop in python
# loops are used to perform a specific task for certain number of times

for i in range(0, 11, 1): # for loop contains three parameters # first parameter shows from where the for loop starts
    # second parameter shows to where it should iterate (Note: It should -1 like if it is (10) then it will execute for 9 iterations)
    print(i)

name = "Abhinav" # name string contains name of specific object
for ch in name: # Using for loop for printing each and every character of the string
    print(ch) # printing character on every iteration

array = ["Abhinav", "John the Don", "Pappu", "Ram Lal"] # An array which include name of different persons
for items in array: # Iterating for loop for the items in the array
    print(items) # Printing an item on every iteration

# Printing number to 100 using range in for loop
for i in range(1, 101, 1):
    print(i)

# Printing 2's table without multiplication using for loop (Self Generated Question)
for i in range(2, 21, 2):
    print(i)