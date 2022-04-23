add_numbers = lambda a, b: a+b
multiply_numbers = lambda a, b: a*b
divide_numbers = lambda a, b: a/b

add_result = add_numbers(10, 5)
multiply_result = add_numbers(add_result, 5)
divide_result = add_numbers(multiply_result, 5)

name_list = ["Vári Róbert", "Kiss Elemér", "Nagy Adrienn", "Tóth Barna", "Kiss Elemér Aladár"]

print(sorted(name_list))


def print_name(name):
    return name.split()[-1]


print(sorted(name_list, key=lambda name: name.split()[-1]))