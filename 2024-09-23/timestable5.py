# Get the table size from the user
size = int(input('Please enter table size: '))

# Print the column titles
print('  x  ', end='')
for column in range(1, size + 1):
    print(f'{column:4}', end='')
print()

# Print the line under the column titles
print('    +', end='')
for column in range(1, size + 1):
    print('----', end='')
print()

for row in range(1, size + 1):
    print(f'{row:3} |', end='')
    for column in range(1, size + 1):
        print(f'{row*column:4}', end='')
    print()