def factorial(n: int) -> int:
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(6))