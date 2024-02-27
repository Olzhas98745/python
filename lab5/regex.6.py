
with open("lab 5/row.txt", "r") as file:
    txt=file.read()
x=txt.replace(" ",":").replace(",",":" ).replace(".",":")
with open ("lab 5/row.txt","w") as file:
    file.write(x)
print(x)