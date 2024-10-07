import math

def solve(a: float, b: float) -> int:
    if a > b:
        a, b = b, a
    a = math.ceil(a)
    b = math.floor(b)
    return sum(range(a, b + 1))