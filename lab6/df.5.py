a = input()
lists = [i for i in a.split()]
file = open(r"C:\Users\Asus\work\lab6\B.txt","w")
for s in lists:
    file.write(s + ' ')
file.close()