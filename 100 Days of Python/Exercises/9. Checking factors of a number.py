user = int(input("Enter a Number: "))
factors = []

def factor():
    for i in range(1, user+1):
        if user%i==0:
            factors.append(i)
    return factors

print(factor())