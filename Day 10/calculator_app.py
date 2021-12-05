# Calculator App


def add(f_number, s_number):
    return f_number + s_number


def subtract(f_number, s_number):
    return f_number - s_number


def multiply(f_number, s_number):
    return f_number * s_number


def divide(f_number, s_number):
    return f_number / s_number


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    number1 = float(input("What is your first number?. \n"))

    for symbol in operations:
        print(symbol)

    app_continue = True

    while app_continue:
        user_operation = input("Pick an operation: ")
        number2 = float(input("What is the next number?. \n"))

        if user_operation == "+":
            result = add(number1, number2)
        elif user_operation == "-":
            result = subtract(number1, number2)
        elif user_operation == "*":
            result = multiply(number1, number2)
        elif user_operation == "/":
            result = divide(number1, number2)

        print(f"{number1} {user_operation} {number2} = {result}")
        if input(f'Type "Yes" for continue calculating with {result}: \n') == "Yes":
            number1 = result
        else:
            app_continue = False
            calculator()


calculator()
