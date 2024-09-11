num = int(input('Please enter a number in the range 1...10: '))
if num < 1:
    print('Number is too low')
else:
    if num > 10:
        print('Number is too high')
    else:
        print('I can accept that number')