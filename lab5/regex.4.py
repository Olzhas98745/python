import re
def find_sequences(text):
    pattern=re.compile(r'[A-Z][a+z]+')
    sequences=pattern.findall(text)
    return sequences
    

with open("lab 5/row.txt","r") as file:
   x=file.read()
sequences=find_sequences(x)
if sequences:
    print(sequences)
else:
    print("NO SEQUENCES")