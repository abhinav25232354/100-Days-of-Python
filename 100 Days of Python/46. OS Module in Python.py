# By using OS module we can take control over OS functions
import os

if (not os.path.exists("Data")):
    os.mkdir("Data")
    # os.mkdir(f"Data/Day{i}")

else:
    for i in range(0, 11):
        # os.mkdir(f"Data/Day{i}")
        # os.rename(f"Data/Day{i}", f"Data/Day {i}")
        print(os.listdir(f"Data/Day {i}"))
    print(f"Folder: ")