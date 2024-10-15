from typing import Callable

def add(x: float, y: float) -> float:
    """ Adds the parameters x and y """
    return x + y

def multiply(x: float, y: float) -> float:
    """ Multiplies the parameters x and y """
    return x * y

def evaluate(f: Callable[[float, float], float], 
             x: float, y: float) -> float:
    """ Calls the function f with parameters x 
        and y: f(x, y) """
    return f(x, y)


print(evaluate(add, 2, 3))
print(evaluate(multiply, 2, 3))