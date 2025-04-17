vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
user = input("Enter a Word: ")
count = 0

for i in range(0, len(user), 1):
    if user[i] in vowels:
        print(user[i])
        count += 1

print(count)