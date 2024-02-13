from itertools import permutations
"""import a function permutations
from the itertools module.
permutations generates
all possible permutations of elements"""
def print_permutations():
    s = input("String : ")
    perms = permutations(s) 
    print("All permutations : ")
    for perm in perms:
        print(''.join(perm))
        
print_permutations()
