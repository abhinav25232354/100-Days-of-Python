num = int(input("Enter a number: "))
#153
a = num%10 #3
b = num//10 #15
c = b%10 #5
d = b//10 #1
z = a**3 + c**3 + d**3
print(a)
print(c)
print(d)
if z==num:
    print("Number is Armstrong")
else:
    print("It is not a Armstrong Number")