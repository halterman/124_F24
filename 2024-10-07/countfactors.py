
def count_factors(n: int) -> int:
    """
    Counts the number of factors in the
    non-negative integer n. The function
    returns zero if n is zero or negative.
    """
    factors = 0
    print(factors)
    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1
            
    return factors

factors = 19
print(factors)
x = '100'
print(count_factors(x))
print(count_factors(13))
print(count_factors(25))

