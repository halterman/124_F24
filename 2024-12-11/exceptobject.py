import random

def process():
    r = random.randint(1, 3) # r is 1, 2, or 3
    if r == 1:
        print(int('Fred')) # Try to convert a non-integer
    elif r == 2:
        [][2] = 5  # Non-existent index of the empty list
    else:
        print(3/0) # Try to divide by zero
    

if __name__ == '__main__':
    try:
        process()
    except ValueError as e:
        print(f'Problem with a value <{e}>')
    except IndexError as e:
        print(f'List index is out of range <{e}>')
    except ZeroDivisionError as e:
        print(f'Division by zero not allowed <{e}>')
    except Exception as e:
        print(f'Some other error occurred <{e}>')
