from typing import Generator


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for potential_factor in range(3, n, 2):
        if n % potential_factor == 0:
            return False
    return True

def prime_generator(begin: int, end: int) -> Generator[int, None, None]:
    for i in range(begin, end + 1):
        if is_prime(i):
            yield i


if __name__ == '__main__':
    
    for num in range(150):
        if is_prime(num):
            print(num, end=' ')
    print()
    
    print('--------------------------')
    
    for num in prime_generator(-10, 150):
        print(num, end=' ')
    print()

