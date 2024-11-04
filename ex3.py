import numpy as np
from exercise_class_init import Exercise

class ex3(Exercise):
    def __init__(self, matrix):
        if not isinstance(matrix, np.ndarray):
            raise ValueError("Input must be a numpy array")
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Matrix must be square")
        self.matrix = matrix
        super().__init__()

    def solve(self):
        local_minima = []
        rows, cols = self.matrix.shape

        for i in range(rows):
            for j in range(cols):
                current = self.matrix[i, j]
                is_minimum = True

                # Check top
                if i > 0 and self.matrix[i - 1, j] <= current:
                    is_minimum = False
                # Check bottom
                if i < rows - 1 and self.matrix[i + 1, j] <= current:
                    is_minimum = False
                # Check left
                if j > 0 and self.matrix[i, j - 1] <= current:
                    is_minimum = False
                # Check right
                if j < cols - 1 and self.matrix[i, j + 1] <= current:
                    is_minimum = False

                if is_minimum:
                    local_minima.append((i, j))

        return local_minima
