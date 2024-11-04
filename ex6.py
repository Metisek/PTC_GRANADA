from exercise_class_init import Exercise

class ex6(Exercise):
    def __init__(self, M, N):
        if not isinstance(N, int) and not isinstance(M, int):
            raise TypeError('Arguments must be integers')
        self.N = N
        self.M = M
        super().__init__()

    def solve(self):
        matrix = [[i + j * (self.N + 1) + 1 for j in range(self.N)] for i in range(self.M)]
        transpose_matrix = [[matrix[j][i] for j in range(self.M)] for i in range(self.N)]
        return transpose_matrix
