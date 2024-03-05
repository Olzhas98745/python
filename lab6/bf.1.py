a=set()
n=int(input())
for _ in range(n):
    x = int(input())
    a.add(x)
print("My set: ", a)
b=1
for i in a:
    b=b*i
print("Product: ",b)