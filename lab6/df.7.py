with open('A.txt', 'r') as firstfile, open('B.txt', 'a') as secondfile:
    for row in firstfile:
        secondfile.write(row)