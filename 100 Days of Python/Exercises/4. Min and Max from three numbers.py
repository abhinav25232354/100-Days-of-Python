a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a>b and a>c:
    print(f"{a} is greatest of all")
elif b>a and b>c:
    print(f"{b} is greatest of all")
elif c>a and c>b:
    print(f"{c} is greatest of all")
else:
    print("Invalid input")