import numpy as np
from exercise_class_init import Exercise
import matplotlib.pyplot as plt
import os
from matplotlib.animation import FuncAnimation

class ex3(Exercise):
    def __init__(self, file_out_path: str):
        if not isinstance(file_out_path, str):
            raise TypeError("File out path must be a string.")
        abs_folder_path = os.path.dirname(os.path.abspath(file_out_path))
        if not os.path.exists(abs_folder_path):
            raise FileNotFoundError(f"The folder {abs_folder_path} does not exist.")
        self.file_out_path = file_out_path
        super().__init__()

    def solve(self):

        # Define the function to animate
        def animate(i):
            x = np.linspace(0, 2 * np.pi, 1000)
            y = np.sin(x + i / 10.0)
            line.set_data(x, y)
            return line,

        # Create a figure and axis
        fig, ax = plt.subplots()
        ax.set_xlim(0, 2 * np.pi)
        ax.set_ylim(-1, 1)
        line, = ax.plot([], [], lw=2)

        # Create the animation
        ani = FuncAnimation(fig, animate, frames=200, interval=20, blit=True)
        ani.save(self.file_out_path, writer='imagemagick')

        # Display the animation
        plt.show()
