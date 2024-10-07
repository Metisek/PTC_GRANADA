def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def solve(year: int) -> int:
    if not isinstance(year, int) or year < 0:
        raise ValueError("Year must be a non-negative integer")

    if is_leap_year(year):
        return year

    next_year = year + 1
    prev_year = year - 1

    while True:
        if is_leap_year(next_year):
            return next_year
        if is_leap_year(prev_year):
            return prev_year
        next_year += 1
        prev_year -= 1
