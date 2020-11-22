def is_number(input_number):
    try:
        number = float(input_number)
        if number >= 0:
            return number
    except ValueError:
        pass
    except TypeError:
        pass
    return None


def is_valid_operator(operator):
    operators = ('+', '-', '*', '/')
    return operator in operators


def ask_for_a_number(force_valid_input):    
    while True:
        number = is_number(input("Please provide a number: "))
        if(number == None and force_valid_input):
            print("This didn't look like a number,try again")
            continue
        
        return number


def ask_for_an_operator(force_valid_input):
    while True:
        operator = (input("Please provide an operator(one of: +, -, *, /): "))
        valid_operator = is_valid_operator(operator)
        if(not valid_operator and force_valid_input):
            print("Unknown operator")
            continue

        return operator if valid_operator else None


def calc(operator, a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return None

    if(not is_valid_operator(operator)):
        return None

    if(operator == '+'):
        result = a + b
    if(operator == '-'):
        result = a - b
    if(operator == '*'):
        result = a * b
    if(operator == '/'):
        if b == 0:
            print("Division by zero")
            return None
        result = a / b
    
    return round(result, 2)

def simple_calculator():
    pass


if __name__ == '__main__':
    simple_calculator()





result = calc('/', '2.3', '3.3')
print(result)
