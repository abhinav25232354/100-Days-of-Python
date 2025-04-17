# Understanding the arguments in python
def average(a, b):
    avg = a+b/2
    print(f"Average: {avg}")

average(5, 9)

# Using default argument
def average(a=9, b=2):
    avg = a+b/2
    print(f"Average: {avg}")

average() # Function will be called with default arguments
average(5, 9) # Function will be called with these values

# Using keyword argument - No sequence bound
def average(a=9, b=2):
    avg = a+b/2
    print(f"Average: {avg}")

average(b=5, a=9) # Function will be called with these values

# Iterative arguments
def avg(*number): # Stores arguments as tuples which are immutable
    print(f"Iterative Arguments: {number}")

avg(5, 6, 7, 7, 8)
# avg(5, 6, 7)
# avg(5, 6, 7, 8)
# avg(5, 6, 7, 8, 9)
# avg(5, 6, 7, 8, 9, 10)

# Arguments as dictionary
def sum(**num): # Stores arguments as dictionary key-value pairs
    print(num)
    print(num["name"])
    print(num["age"])

sum(name="Abhinav", age=18)

# Note: return statement return with taking the value to the function at initialization
# Like:-
def returntypefunction(a, b):
    c = a+b
    return c
z = returntypefunction(12, 8)
print(z)