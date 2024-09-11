print('Version 2')
num = int(input('Please enter an integer in the range 1...5, inclusive: '))
if 1 <= num <= 5:
    if num == 1:
        print('one')
    elif num == 2:
        print('two')
    elif num == 3:
        print('three')
    elif num == 4:
        print('four')
    elif num == 5:
        print('five')
else:
    print('Number is out of range')