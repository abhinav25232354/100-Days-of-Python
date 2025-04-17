# Decision making using python

# Driving check
age = int(input("Enter your age: ")) # Taking input of age of the user
print("Your age is,", age) # Printing the age for verification by user

if age>18: # Checking if age is greater than 18 or not
    print("You are eligible for driving license")
elif age<18: # checking if the age is less than 18 or not
    print("You cannot drive at this age")
elif age==18: # Checking if the age is equal to 18
    print("You are eligible for driving license")
else:
    print("Invalid input of age")

# There is if-else ladder also which include if-else under if-else