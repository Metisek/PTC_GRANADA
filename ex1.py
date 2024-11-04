import numpy as np
from exercise_class_init import Exercise

class ex1(Exercise):
    def __init__(self):
        super().__init__()

    def solve(self):
        # Generate a random matrix of 10 rows and 4 columns using a normal distribution
        matrix = np.random.randn(10, 4)

        # Apply min-max normalization to each row
        min_vals = matrix.min(axis=1, keepdims=True)
        max_vals = matrix.max(axis=1, keepdims=True)
        normalized_matrix = (matrix - min_vals) / (max_vals - min_vals)

        # Sort the matrix in descending order from the last column
        sorted_matrix = normalized_matrix[normalized_matrix[:, -1].argsort()[::-1]]
        return sorted_matrix
