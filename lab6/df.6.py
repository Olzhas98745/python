import string
import os


directory_path = r"C:\Users\Asus\work\lab6"

for letter in string.ascii_uppercase:
    file_path = directory_path + "\\" + letter + ".txt"
    with open(file_path, 'w') as file:

        file.write("Content of " + letter + ".txt\n")

print("Text files created successfully.")