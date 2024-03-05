a=input()
u=0
s=0

for i in a:
    if i.isupper():
        u+=1
    else:
        s+=1
print("Upper: ", u)
print("Lower: ", s)