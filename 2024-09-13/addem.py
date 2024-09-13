# Add up an arbitrary number of nonnegative integers

print('Please enter some nonnegative integers (-1) quits')
sum = 0
not_done = True
while not_done:
    in_val = int(input('=> '))
    if in_val >= 0:
        sum += in_val
    else:
        not_done = False

print(f'The sum of the numbers is {sum}.')