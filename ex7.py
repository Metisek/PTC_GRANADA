from exercise_class_init import Exercise
import random

class ex7(Exercise):
    def __init__(self, M, N):
        if not isinstance(N, int) and not isinstance(M, int):
            raise TypeError('Arguments must be integers')
        self.N = N
        self.M = M
        super().__init__()

    def solve(self):
        list1 = [random.randint(1, 10) for _ in range(self.N)]
        list2 = [random.randint(1, 10) for _ in range(self.M)]
        intersection = sorted(set(list1) & set(list2))
        print(f"List 1: {list1}")
        print(f"List 2: {list2}")
        return intersection
