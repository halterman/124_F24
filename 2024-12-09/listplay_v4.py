from random import randrange

def make_list() -> list[int]:
    return [randrange(0, 100) for _ in range(randrange(1, 10))]

# for _ in range(20):
#     print(make_list())

lst = make_list()
print(f'The secret list is {lst}')  # TODO remove this
try:
    idx = int(input('Please enter position:'))
    print(lst[idx])
except:
    print('Something went wrong')
