# contains method to parse user input into lambda function
import numpy as np
from sympy import lambdify, sympify, symbols


def parse_input(input):
    x = symbols('x')
    symp_function = sympify(input)
    f = lambdify(x, symp_function, "math")

    return f


# test lambdify func
if __name__ == "__main__":
    
    print('\n\n\n\n')
    active = True

    while active == True:
        print('----test func triggered----')
        print('type \'n\' to terminate')
        test_input = input('enter function to be lambdified: ')
        if test_input == 'n':
            active = False
        else:
            print(str(parse_input(test_input)))