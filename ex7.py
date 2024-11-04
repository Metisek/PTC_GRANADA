import numpy as np
from exercise_class_init import Exercise

class ex7(Exercise):
    def __init__(self, vec1, vec2, vec3):
        if not isinstance(vec1, (np.ndarray, list)) or not isinstance(vec2, (np.ndarray, list)) or not isinstance(vec3, (np.ndarray, list)):
            raise TypeError("All vectors must be numpy arrays or lists.")

        if isinstance(vec1, list):
            vec1 = np.array(vec1)
        if isinstance(vec2, list):
            vec2 = np.array(vec2)
        if isinstance(vec3, list):
            vec3 = np.array(vec3)
        if vec1.shape != vec2.shape or vec1.shape != vec3.shape:
            raise ValueError("All vectors must have the same shape.")
        self.vec1 = vec1
        self.vec2 = vec2
        self.vec3 = vec3
        super().__init__()

    def solve(self):
        col_vec = self.vec3.reshape(-1, 1)

        # Using np.multiply and np.matmul
        O = np.outer(self.vec1, self.vec2)
        result_np = np.matmul(O, O.T)
        final_result_np = np.multiply(result_np, col_vec)

        # Using operators * and @
        O_op = np.outer(self.vec1, self.vec2)
        result_op = O_op @ O_op.T
        final_result_op = result_op * col_vec

        return f"final_result_np: {final_result_np},\nfinal_result_op: {final_result_op}"
