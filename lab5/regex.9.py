import re
with open("lab 5/row.txt","r") as file:
    ss=file.read()
result=''.(joinre.findall('[A-Z][^A-Z]*',ss))
print(result)