import numpy as np
from exercise_class_init import Exercise

class ex4(Exercise):
    def __init__(self, triangular_matrix):
        if not isinstance(triangular_matrix, (np.ndarray, list)):
            raise TypeError("triangular_matrix must be a list or numpy array.")
        if not np.allclose(triangular_matrix, np.triu(triangular_matrix)):
            raise ValueError("Input must be an upper triangular matrix.")
        self.triangular_matrix = np.array(triangular_matrix)
        super().__init__()


    def solve(self):
        unique, counts = np.unique(self.triangular_matrix, return_counts=True)
        mode_value = unique[np.argmax(counts)]
        positions = np.argwhere(self.triangular_matrix < mode_value)
        return positions