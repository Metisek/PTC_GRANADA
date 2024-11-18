import numpy as np
from exercise_class_init import Exercise
import matplotlib.pyplot as plt

class ex5(Exercise):
    def __init__(self):
        super().__init__()

    def solve(self):
        months = np.arange(1, 13)
        temperature = [30, 32, 35, 40, 45, 50, 48, 46, 40, 35, 30, 28]
        precipitation = [120, 110, 90, 80, 60, 40, 50, 70, 90, 100, 120, 140]

        fig, ax1 = plt.subplots()

        # Plot bars first (on ax1)
        color = 'tab:blue'
        ax1.bar(months, precipitation, color=color, alpha=0.6, label='Precipitation', zorder=1)
        ax1.set_xlabel('Month')
        ax1.set_ylabel('Precipitation (mm)', color=color)
        ax1.tick_params(axis='y', labelcolor=color)

        # Add twin axis for temperature
        ax2 = ax1.twinx()
        color = 'tab:red'
        ax2.set_ylabel('Temperature (°C)', color=color)
        ax2.plot(months, temperature, color=color, label='Temperature', zorder=2, linewidth=2)
        ax2.tick_params(axis='y', labelcolor=color)

        # Adjust layout and show plot
        fig.tight_layout()
        plt.show()
