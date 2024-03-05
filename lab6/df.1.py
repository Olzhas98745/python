import os

path = r"C:\Users\Asus\work"
print("Directories: ")
for directory in os.listdir(path):
    if os.path.isdir(os.path.join(path, directory)):
        print(directory)
print("/n Files: ")
for filename in os.listdir(path):
    if os.path.isfile(os.path.join(path, filename)):
        print(filename)
print("/n All")
for name in os.listdir(path):
    print(name)