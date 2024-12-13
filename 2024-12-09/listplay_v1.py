from random import randrange

def make_list() -> list[int]:
    return [randrange(0, 100) for _ in range(randrange(0, 10))]

# for _ in range(20):
#     print(make_list())

lst = make_list()
idx = int(input('Please enter position:'))
print(lst[idx])
