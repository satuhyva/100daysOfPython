import art

print(art.logo)

def get_number(order):
    number = input(f"What is the {order} number? ")
    if not number.isdecimal():
        print("Number must be a number!")
        return get_number(order)
    return int(number)

def get_operator():
    operator = input("+, -, * or / ? Pick an operator: ")
    if operator not in ['+', '-', '*', '/']:
        print("Operator must be +, -, * or /. ")
        return get_operator()
    return operator

def calculate(number1, number2, operator):
    if operator == '/' and number2 == 0:
        print("Cannot divide by zero!")
        return None
    result = 0
    if operator == '+':
        result = number1 + number2
    if operator == '-':
        result = number1 - number2
    if operator == '*':
        result = number1 * number2
    if operator == '/':
        result = number1 / number2
    print(f"{number1:.1f} {operator} {number2:.1f} = {result:.1f}")
    return result

numberMemo = None

while True:
    number1 = numberMemo
    if number1 == None:
        number1 = get_number("first")
    operator = get_operator()
    number2 = get_number("second")
    result = calculate(number1, number2, operator)

    go_further = input("Want to continue with this result as the first number (y or n)? ")
    if go_further == 'y':
        numberMemo = result
    else:
        numberMemo = None
        go_again = input("Go again (y or n)? ")
        if not go_again == 'y':
            break   
    
    