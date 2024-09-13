print('Version 4')
num = int(input('Please enter an integer in the range 1...5, inclusive: '))
match num:
    case 1: 
        print('one')
    case 2: 
        print('two')
    case 3: 
        print('three')
    case 4: 
        print('four')
    case 5: 
        print('five')
    case _:
        print('Number is out of range')