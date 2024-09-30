# Copy of the square root program we wrote on 2024-09-16.

i = float(input('Please enter number: '))

r = 1
while abs(r*r -  i) > 0.0000001:
    r = (r + i/r)/2
    print(f'r is currently {r}')

print(f'The square root of {i} is {r}')
