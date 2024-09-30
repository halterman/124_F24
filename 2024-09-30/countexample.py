
# Function definition
def count(n: int) -> None:
    s = 7
    for i in range(n):
        print(i)

print(s)

def no_params() -> None:
    print('Function that has no parameters')

def twice(x: float) -> float:
    print(f'x = {x}')
    r = range(10)
    return 2 * x

# Function invocation
# count(5)
# number = 9
# count(number)
# no_params()

# double = twice(number);
# print(f'Twice {number} is {double}')

# count(6)

