def all_true(elements):
    return all(elements)

user_input = input()
my_tuple = tuple(map(bool, map(int, user_input.split())))

result = all_true(my_tuple)

print(result)
