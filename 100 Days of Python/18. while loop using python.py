i = 0
while(i<3):
    print(i)
    i = i+1

# Using for advance condition
print("Guess the number which is matching to the integrated number in the program hint: num>10 and num<20")
num = int(input("Guess a number: "))
print(num)
while (num<=18):
    num = int(input("Guess a number: "))
    print(num)

# Reverse while loop
number = 10
while (number>=0):
    print(number)
    number -= 1

# We can use else with the while loop
# When while loop condition is false then it will execute else
'''
i = 0
while (i<=10):
    print(i)
    i += 1
else:
    print("Conditiont not satisfied")
'''

# Emulating do while loop in python
# Treating this two lines of code as do-while loop content

# do {
integer = int(input("Enter a number: "))
print(integer)
# }

# While condition
while (integer<=10):
    print("Enter a number: ")
    print(integer)