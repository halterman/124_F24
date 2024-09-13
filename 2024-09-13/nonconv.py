x = int(input('Enter a number: '))
y = int(input('Enter another number: '))
z = int(input('Enter a third number: '))

if x == 1:
    print(f'x is {x}')
elif y > 1000:
    print(f'y is large')
elif z == 1:
    print(f'z is {z}')
else:
    print('Using neither x, y, nor z')