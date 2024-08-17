# contains method to parse user input into lambda function
import numpy as np
from sympy import lambdify, sympify, symbols


def parse_input(input):
    x = symbols('x')
    symp_function = sympify(input)
    f = lambdify(x, symp_function, "math")

    return f