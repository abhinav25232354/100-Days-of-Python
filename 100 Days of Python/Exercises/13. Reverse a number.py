n = int(input("Enter a Number: "))
# print(n[0])
reverse = 0

while n>0:
    digit = n%10
    reverse = reverse*10 + digit
    n //= 10

print(reverse)