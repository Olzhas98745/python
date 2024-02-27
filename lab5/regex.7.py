def snaketocamel(snakecase):
    parts=snakecase.split('_')
    camelcase=parts[0]+''.join(x.capitalize() for x in parts [1:])
    return camelcase
with open("lab 5/row.txt","r") as file:
    snakecasestr=file.read()
camelcasestr=snaketocamel(snakecasestr)
print(camelcasestr)