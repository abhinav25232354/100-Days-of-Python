# read - for reading whole file at once
# readlines -  read all lines of a iterable object
# readline - read single line
# writelines - write lines if object is iterable

f = open("F:/100 Days of Python/Data/Day 2/Hello.txt", "r")
text = f.read()
line = f.readline()
lines = f.readlines()
print(text)
print(line)
print(lines)

# writelines
list = ["Hello", "I", "am", "Abhinav"]
with open("F:/100 Days of Python/Data/Day 2/Hello.txt", "w") as f:
    f.writelines(list)
    f.close()
