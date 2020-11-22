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
    pass


def simple_calculator():
    pass


if __name__ == '__main__':
    simple_calculator()





operator = ask_for_an_operator(False)

print(operator)
