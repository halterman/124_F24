num1 = float(input('Please enter a number: '))
num2 = float(input('Please enter another number: '))

r1 = 1
while abs(r1*r1 -  num1) > 0.0000001:
    r1 = (r1 + num1/r1)/2

r2 = 1
while abs(r2*r2 -  num2) > 0.0000001:
    r2 = (r2 + num2/r2)/2

print(f'root({num1}) + root({num2}) = {round(r1 + r2, 2)}')