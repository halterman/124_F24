def reverse(a: list[int]) -> None:
    n = len(a)
    halfway = n // 2
    for i in range(0, halfway):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]


def sort(a: list[int]) -> None:
    n = len(a)
    for i in range(0, n - 1):
        smallest = i
        for j in range(i + 1, n):
            if a[j] < a[smallest]:
                smallest = j
        if smallest != i:
            a[i], a[smallest] = a[smallest], a[i]
            # Most programming languages do not support
            # tuple assignment, so you have to do this:
            # temp = a[i]
            # a[i] = a[smallest]
            # a[smallest] = temp

