list = [656, 557, 989, 234, 645]
print(list)
list.sort()
print(list)
max = 0

for i in range(0, len(list), 1):
    if list[i]>max:
        max = list[i]
    
print(max)