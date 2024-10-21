from typing import Generator

def generate_multiples(m: int, n: int) -> Generator[int, None, None]:
    count = 0
    while count < n:
        yield m * count
        count += 1

