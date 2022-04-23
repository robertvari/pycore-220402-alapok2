def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    return a / b


add_result = add_numbers(10, 5)
multiply_result = multiply_numbers(add_result, 5)
divide_result = divide_numbers(multiply_result, 5)

print(divide_result)