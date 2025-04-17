# lambda function in python are anonymous function
# Lambda function are single line functions useful for small functions

sum = lambda a, b: print(f"Addition {a, b}: {a + b}")
subtract = lambda a, b: print(f"Subtraction {a, b}: {a - b}")
multiply = lambda a, b: print(f"Multiplication {a, b}: {a * b}")
divide = lambda a, b: print(f"Division {a, b}: {a / b}")
modulas = lambda a, b: print(f"Modulas {a, b}: {a % b}")
floor = lambda a, b: print(f"Floor Division {a, b}: {a // b}")
avg = lambda a, b, c: print(f"Average {a, b, c}: {(a + b + c)/3}")
sum(2, 4)
subtract(2, 4)
multiply(2, 4)
divide(2, 4)
modulas(2, 4)
floor(2, 4)
avg(2, 4, 4)

# can be used as arguments for multiple line functions
def square(x, y):
    return x(y*y)

# x = 2
print(square(lambda x: x*x, 4)) # taking substitute as 16 square of 4 
