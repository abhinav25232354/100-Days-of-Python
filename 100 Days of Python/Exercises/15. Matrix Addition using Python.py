m = int(input("Enter m: "))
n = int(input("Enter n: "))
a = []
b = []

for i in range(m):
    for j in range(n):
        a_in = int(input(f"Enter A[{i}][{j}]: "))
        a.append(a_in)

for i in range(m):
    for j in range(n):
        b_in = int(input(f"Enter B[{i}][{j}]: "))
        b.append(b_in)

for i in range(m):
    for j in range(n):
        print(a_in)

for i in range(m):
    for j in range(n):
        print(b_in)
    
