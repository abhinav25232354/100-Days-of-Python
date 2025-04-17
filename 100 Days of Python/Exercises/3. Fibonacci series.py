# For making this i have use a logic which says take a, b and calculate c for the addition of a+b
n = int(input("Enter a number: "))
a = 0
b = 1
c = a+b
print(a)
print(b)
print(c)
for i in range(0, n, 1):
    a = b
    b = c
    c = a+b
    # if c>100:
    #     break
    print(c)