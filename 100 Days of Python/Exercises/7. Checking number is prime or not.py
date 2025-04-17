n = int(input("Enter a Number: "))

for i in range(n-1, 1, -1):
    # if n%i != 0:
    if n%i == 0:
        print("Number is not Prime Number")
        break
else:
    print("Number is Prime Number")