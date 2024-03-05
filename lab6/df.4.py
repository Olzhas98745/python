import os
path = r'C:\Users\Asus\work\lab6\A.txt'
with open(path, 'r') as c:
    lines = len(c.readlines())
    print(lines)