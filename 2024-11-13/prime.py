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
