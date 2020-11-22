def is_number(input_number):
    try:
        number = int(input_number)
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
    pass


def ask_for_an_operator(force_valid_input):
    pass


def calc(operator, a, b):
    pass


def simple_calculator():
    pass


if __name__ == '__main__':
    simple_calculator()


# +, -, *, /, 1, a, None, '' ' '
result = is_valid_operator('*')
print(result)