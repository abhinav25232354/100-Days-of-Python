# append method
list = [1, 2, 3, 4, 5]
print(list)
list.append(8)
print(list)

# sorting
list.sort()
print(list)
list.sort(reverse=True)
print(list)

# printing index
print(list.index(2))

# count number of iteration of of specific value
print(list.count(2))

#copy method
m = list.copy()
m[0] = 0
print(list) # list will be same

# list.insert(1, 989) # It will place 989 at 1st index place
# n = [98, 978, 65, 76, 54]
# list.extend(n) # It will add n to the end of n