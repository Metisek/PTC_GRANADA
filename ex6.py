def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def solve(n, k):
    if k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))