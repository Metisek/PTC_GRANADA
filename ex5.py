import numpy as np
from exercise_class_init import Exercise

class ex5(Exercise):
    def __init__(self, vector):
        if not isinstance(vector, (np.ndarray, list)):
            raise TypeError("Vector must be a list or numpy array.")
        self.vector = np.array(vector)
        super().__init__()

    def solve(self):

        for i in range(len(self.vector)):
            if self.vector[i] % 0.5 == 0:
                self.vector[i] += 1

            elif abs(self.vector[i]) > 4.7:
                self.vector[i] = round(self.vector[i])

        # Extract the first 20 values as a row vector
        row_vector = self.vector[:20].reshape(1, -1)

        # Extract the last 20 values as a column vector
        column_vector = self.vector[-20:].reshape(-1, 1)

        # Perform matrix multiplication
        result = np.dot(row_vector, column_vector)

        # Return the result
        return result[0][0]