import numpy as np
from exercise_class_init import Exercise

class ex6(Exercise):
    def __init__(self, A, B):
        if not isinstance(A, (list, np.ndarray)) or not isinstance(B, (list, np.ndarray)):
            raise TypeError("A and B must be either lists or numpy arrays.")
        if isinstance(A, list):
            A = np.array(A)
        if isinstance(B, list):
            B = np.array(B)
        if A.shape[0] != A.shape[1] or A.shape[0] != B.shape[0]:
            raise ValueError("A must be a square matrix and B must have the same number of rows as A.")

        self.A = A
        self.B = B

    def solve(self):
        augmented_matrix = np.hstack((self.A, self.B.reshape(-1, 1)))
        rank_A = np.linalg.matrix_rank(self.A)
        rank_augmented = np.linalg.matrix_rank(augmented_matrix)

        if rank_A == rank_augmented:
            if rank_A == self.A.shape[0]:
                solution = np.linalg.solve(self.A, self.B)
                return solution
            else:
                return "The system has infinitely many solutions."
        else:
            return "The system is incompatible and has no solutions."