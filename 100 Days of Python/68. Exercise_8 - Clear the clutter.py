import os

# folder = "C:\\Users\\abhin\\AppData\\Local\\Temp"  # replace with your folder name
folder = "my folder"

for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    os.remove(file_path)
    print(f"Deleted {file}")