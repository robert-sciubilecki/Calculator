def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations_dict = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator(a, operation, b):
    return operations_dict[operation](a, b)


def print_result(a, operation, b, op_sum):
    print(f'The result of {a} {operation} {b} is {op_sum}')


def calculator_func(sub, f_run):
    """Calculator function that takes two arguments
    The fist is sub_sum of previous operations which is needed when continuing calculations
    The second provides the information if the calculator has to perform first or subsequent operation"""
    sub_sum = sub
    first_run = f_run

    if first_run:
        n1 = float(input("What's the first number?: "))
        print(f"Which of the above operations you want to perform?")
        for operation_char in operations_dict:
            print(operation_char)
        user_operation = input('')
        n2 = float(input("What's the second number?: "))
        sub_sum = calculator(n1, user_operation, n2)
        print_result(n1, user_operation, n2, sub_sum)
        first_run = False

    continue_calc = input(f"Type 'y' to continue calculating with {sub_sum}, "
                          f"or type 'n' to exit. Type 'c' to start over: ").lower()
    if continue_calc == 'n':
        print('Ok, bye.')
        return
    elif continue_calc == 'c':
        calculator_func(sub_sum, True)
    elif continue_calc == 'y':
        user_operation = input('Pick another operation: ')
        n3 = float(input("What's the next number?: "))
        new_sum = calculator(sub_sum, user_operation, n3)
        print_result(sub_sum, user_operation, n3, new_sum)
        calculator_func(new_sum, False)
    else:
        print('Wrong command.')
        calculator_func(sub_sum, False)


calculator_func(None, True)