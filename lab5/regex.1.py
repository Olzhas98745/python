def match_pattern(text):
    pattern=re.compile(r'ab*')
    if pattern.fullmatch(text):
        return True
    else:
        return False

with open("lab 5/row.txt","r") as file:
   x=file.read()

print(match_pattern(x))