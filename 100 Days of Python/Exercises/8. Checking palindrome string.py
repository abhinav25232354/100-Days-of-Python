string = input("Enter a Word: ")
reverse_string = string[::-1]

print(string)
print(reverse_string)

if string==reverse_string:
    print("This is a palindrome string")
else:
    print("It's not Palindrome string")