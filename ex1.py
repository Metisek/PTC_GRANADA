def solve(a: float, b: float) -> float:
    try:
        a, b = float(a), float(b)
    except ValueError:
        raise ValueError('Arguments must be numbers')
    return [a, b] if a > b else [b, a]