# Making a Python program which greets using time and if-else statements
import datetime

hour = datetime.datetime.now().hour # fetching hour from datetime module
minute = datetime.datetime.now().minute # fetching minute from datetime module
seconds = datetime.datetime.now().second # fetching seconds from datetime module
# print(hour) # Printing hours fetched from the module
# print(minute) # Printing minutes fetched from the module
# print(seconds) # Printing seconds fetched from the module
print(f"{hour}:{minute}:{seconds}")

if hour>=0 and hour<=12:
    print("Good Morning Sir")
elif hour>=12 and hour<=18:
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")