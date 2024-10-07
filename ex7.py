# I don't think I understand this task properly.

def solve(number: int) -> int:
    try:
        if not isinstance(number, int):
            raise ValueError("Input must be an integer")
    except ValueError as e:
        print(e)
        return -1
    while number % 9 != 0:
        number -= 1
    return number
