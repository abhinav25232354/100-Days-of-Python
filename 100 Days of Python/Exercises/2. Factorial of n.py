n = int(input("Enter a number: "))

for i in range(n-1, 1, -1):
    n *= i

print(f"Factorial: {n}")