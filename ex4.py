import numpy as np
from exercise_class_init import Exercise
import matplotlib.pyplot as plt

class ex4(Exercise):
    def __init__(self):
        super().__init__()

    def solve(self):
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        x, y = np.meshgrid(x, y)
        z = np.cos(np.sqrt(x**2 + y**2))

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(x, y, z, cmap='viridis')

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.set_title('3D Surface Plot')

        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
        ax.view_init(elev=30, azim=45)

        plt.show()