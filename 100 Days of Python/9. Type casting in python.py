# Changing Data type is known as typecasting
'''
Two types of typecasting
1. Explicit conversion - conversion whcih programmer does by itself
2. Implicit conversion - conversion which python done by itself (Python change data type of higher level data type for preventing data loss)

'''

a = "1"
b = "2"
print(a+b) # 12 (Treated as string concatination)

a1 = "1"
a2 = "2"
print(int(a1) + int(a2)) # 3 (Treated as integer addition)