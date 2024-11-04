from exercise_class_init import Exercise

class ex10(Exercise):
    def __init__(self, N):
        if not isinstance(N, int):
            raise ValueError("N must be an integer")
        self.N = N
        super().__init__()

    def solve(self):

        prime_factors = self.prime_factor_decomposition(self.N)
        print(f"Prime factor decomposition of {self.N}:", end=" ")
        return prime_factors

    def prime_factor_decomposition(self, n):
        if n < 2:
            return []
        factors = []
        i = 2
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 1
        if n > 1:  # If n is still greater than 1, it is prime
            factors.append(n)
        return factors
