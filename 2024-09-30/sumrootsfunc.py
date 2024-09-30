def root(x: float) -> float:
    r = 1
    while abs(r*r - x) > 0.0000001:
        r = (r + x/r)/2
    return r


num1 = float(input('Please enter a number: '))
num2 = float(input('Please enter another number: '))

print(f'root({num1}) + root({num2}) = {round(root(num1) + root(num2), 2)}')