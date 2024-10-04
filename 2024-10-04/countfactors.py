def count_factors(n: int) -> int:
    factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1
            
    return factors

print(count_factors(24))
print(count_factors(13))
print(count_factors(25))
