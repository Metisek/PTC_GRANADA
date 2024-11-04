import numpy as np
from exercise_class_init import Exercise

class ex8(Exercise):
    def __init__(self, vector):
        if not isinstance(vector, (np.ndarray, list)):
            raise TypeError("Vector must be a list or numpy array.")
        self.vector = np.array(vector)
        super().__init__()

    def solve(self):
        window_3 = np.lib.stride_tricks.sliding_window_view(self.vector, window_shape=3).mean(axis=-1)
        window_5 = np.lib.stride_tricks.sliding_window_view(self.vector, window_shape=5).mean(axis=-1)

        last_10_window_3 = window_3[-10:]
        last_10_window_5 = window_5[-10:]

        result = np.column_stack((last_10_window_3, last_10_window_5))
        return result