# File Handling using Python

f = open("F:/100 Days of Python/Data/Day 2/Hello.py", "r")
text = f.read()
print(text)
f.close()

# r - Read mode only read and if file does not exists then throw error
# w - write mode and file can be generated from this mode
# a - append mode, Write text appending at the end of the code
# x - Creation mode, used to create new file
# t - apart from mode, this specify that content is text formatted or binary (Generally text)
# b - binary mode, used to handle binary files, like images and pdfs and anything which is binary


# Note: If we not want to close the file after use we can use "with keyword"
# with open("file.txt", "r"):
    # print("I am inside the with keyword statement")