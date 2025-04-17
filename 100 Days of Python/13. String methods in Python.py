# Operation in a string using python

a = "Abhinav!!!!!! !!!!! abhinav"
print(len(a)) # Length of a variable
print(a.upper()) # Converting a variable into uppercase
print(a.lower()) # converting a variable into lowercase
print(a.rstrip("!"))
print(a.replace("Abhinav", "John the Don"))
print(a.split()) # Make every word a different list element
print(a.capitalize()) # Capitalize first letter of the string

heading = "Welcome to python repl !"
print(len(heading))
print(heading.center(50)) # Move string to center
print(heading.count("o")) # Count the number of iteration of specific word or alphabet in a string
print(heading.endswith("!"))
print(heading.endswith("to", 4, 10)) # Search for to in between the given index
print(heading.find("python")) # it will return the first index of demanded string like - p's index (if the value don't exist then it will return (-1)
print(heading.index("python"))
print(heading.isalnum()) #  is it a alphanumeric string (string which contain A-Z, a-z, 0-9)
print(heading.isalpha()) #  is it a alpha string (string which contain A-Z, a-z)
print(heading.islower()) # is the string lowercase 
print(heading.isprintable()) # is the string printable like (\n, \t)
print(heading.isspace()) # it returns true if there is space in the string
print(heading.istitle()) # checks if first letter is capital or not
print(heading.isupper()) # checks if string is uppercase or not
print(heading.swapcase()) # swap uppercase to lowercase