from utilities.decorators import print_result


@print_result
def add_numbers(a, b):
    return a + b


@print_result
def multiply_numbers(a, b):
    return a * b


@print_result
def divide_numbers(a, b):
    return a / b


add_numbers(10, 5)