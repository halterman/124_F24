def count_evens(a: list[int]) -> int:
    count = 0
    for elem in a:
        if elem % 2 == 0:
            count += 1
    return count


lst = [1, 2, 3, 0, 4, 5, 64, 6, 7]
print(count_evens(lst))