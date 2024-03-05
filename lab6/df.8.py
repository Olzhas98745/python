import os
path  = r'C:\Users\Asus\work\lab6\8.txt'

if os.path.exists(path):
    print("TRUE")
    os.remove(path)
