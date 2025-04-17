# "is" vs "=="
# "is" - Compare exact location of object in memory
# "==" - compare values
a = "Abhinav"
b = "Abhinav"
print(a is b)
print(a == b)

x = 4
y = 4
print(x is y)
print(x == y)

p = [1, 2, 3]
q = [1, 2, 3]
print(p is q) # Because list is mutable, its value can be changed that is why python place both list on different locations
print(p == q)