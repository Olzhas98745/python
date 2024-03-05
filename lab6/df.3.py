import os
path = r'C:\Users\Asus\work'

if os.path.exists(path):
    print([name for name in os.listdir()])
else:
    print("Path does not exist")