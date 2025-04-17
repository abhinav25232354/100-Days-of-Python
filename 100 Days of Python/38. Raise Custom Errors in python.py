# Raise Custom Errors in Python
a = int(input("Enter Number(1-9): "))

if a<1 or a>9:
    raise IndexError("Enter Number Between 1-9")