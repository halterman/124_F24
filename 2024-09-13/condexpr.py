x = int(input('Enter a number: '))
y = int(input('Enter another number: '))

# if x < y:
#     z = x
# else:
#     z = y

# z = x if x < y else y
# print(f'{z} is smaller')


print(f'{x if x < y else y} is smaller')