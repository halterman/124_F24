num = int(input('Please enter an integer in the range 1...5, inclusive: '))
if 1 <= num <= 5:
    if num == 1:
        print('one')
    else:
        if num == 2:
            print('two')
        else:
            if num == 3:
                print('three')
            else:
                if num == 4:
                    print('four')
                else:
                    if num == 5:
                        print('five')
else:
    print('Number is out of range')