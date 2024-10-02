def root(x: float) -> float:
    r = 1
    while abs(r*r - x) > 0.0000001:
        r = (r + x/r)/2
    return r

def twice(x: float) -> float:
    return 2 * x



