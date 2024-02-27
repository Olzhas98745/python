def camel_to_snake(camelcase):
    snakecase = ''
    for char in camelcase:
        if char.isupper():
            snakecase += '_' + char.lower()
        else:
            snakecase += char
    if snakecase.startswith('_'):
        snakecase = snakecase[1:]
    return snakecase

with open('row.txt', 'r') as file:
    lines = file.readlines()


for line in lines:
    snake_line = camel_to_snake(line.strip())
    print(snake_line)

    with open('row_snake.txt', 'a') as file:
        file.write(snake_line + '\n')