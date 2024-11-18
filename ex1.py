import numpy as np
from exercise_class_init import Exercise
import matplotlib.pyplot as plt

class ex1(Exercise):
    def __init__(self, seed: int):
        if not isinstance(seed, int):
            raise TypeError("Seed must be an integer.")
        np.random.seed(seed)
        super().__init__()

    def solve(self):
        # Plot 1: line plot of y = sin(x)
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        plt.subplot(2, 2, 1)
        plt.plot(x, y, 'b', label='y = sin(x)')
        plt.title('Plot 1: y = sin(x)')
        plt.legend()

        # Plot 2: scatter plot of 50 random points in range [0, 1]
        x = np.random.rand(50)
        y = np.random.rand(50)

        plt.subplot(2, 2, 2)
        plt.scatter(x, y, color='g')
        plt.title('Plot 2: 50 random points')
        plt.xlim(0, 1)
        plt.ylim(0, 1)

        # Plot 3:  bar plot of data {"A": 3, "B": 7, "C": 8, "D": 5}
        data = {"A": 3, "B": 7, "C": 8, "D": 5}
        names = list(data.keys())
        values = list(data.values())

        plt.subplot(2, 2, 3)
        plt.bar(names, values, color='purple')
        plt.title('Plot 3: Bar plot')

        # Plot 4: histogram of 1000 random numbers from normal distribution
        data = np.random.randn(1000)

        plt.subplot(2, 2, 4)
        plt.hist(data, bins=25)
        plt.title('Plot 4: Histogram of 1000 random numbers')

        # Adjust layout and show plot
        plt.gcf().set_size_inches(9, 9)
        plt.tight_layout()
        plt.show()
