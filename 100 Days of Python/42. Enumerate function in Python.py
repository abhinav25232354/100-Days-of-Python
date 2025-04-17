# Enumerate function in python
# print index of the element with element itself

names = ["Abhinav", "harry", "Shinchan"]
for index, name in enumerate(names):
    print(f"{index} {name}")

# Change start index
# names = ["Abhinav", "harry", "Shinchan"]
# for index, name in enumerate(names, start=1):
#     print(f"{index} {name}")