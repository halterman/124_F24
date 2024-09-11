num1 = int(input('Please enter the first number: '))
num2 = int(input('Please enter the second number: '))
if num2 != 0:
    ans = num1 / num2
    print(f'{num1} / {num2} = {ans}')
else:
    print('Cannot divide by zero')
print('Program done')