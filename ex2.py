import numpy as np
from exercise_class_init import Exercise

class ex2(Exercise):
    def __init__(self, points_a, points_b):
        if not isinstance(points_a, np.ndarray):
            try:
                points_a = np.array(points_a)
            except TypeError:
                raise TypeError("points_a must be a numpy array")
        if not isinstance(points_b, np.ndarray):
            try:
                points_b = np.array(points_b)
            except TypeError:
                raise TypeError("points_b must be a numpy array")
        if points_a.shape[1] != 2 or points_b.shape[1] != 2:
            raise ValueError("Both arrays must have 2 columns")
        self.points_a = points_a
        self.points_b = points_b
        super().__init__()

    def solve(self):
        diff = self.points_a[:, np.newaxis, :] - self.points_b[np.newaxis, :, :]
        distances = np.sqrt(np.sum(diff**2, axis=-1))
        return distances
