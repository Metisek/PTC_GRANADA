import numpy as np
from exercise_class_init import Exercise
from matplotlib.widgets import Slider, Button
import matplotlib.pyplot as plt

class ex2(Exercise):
    def __init__(self):
        super().__init__()

    def solve(self):
        # Initial parameters
        a_init = 1
        b_init = 1
        x = np.linspace(0, 2 * np.pi, 1000)
        y = a_init * np.sin(b_init * x)

        # Create the plot
        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.1, bottom=0.3)
        line, = ax.plot(x, y, lw=2)
        ax.set_ylim(-2, 2)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Interactive Sine Wave')

        # Create sliders
        ax_amp = plt.axes([0.2, 0.1, 0.65, 0.03])
        ax_freq = plt.axes([0.2, 0.15, 0.65, 0.03])
        slider_amp = Slider(ax_amp, 'Amplitude', 0, 2, valinit=a_init)
        slider_freq = Slider(ax_freq, 'Frequency', 0, 2, valinit=b_init)

        # Create reset button
        resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
        button = Button(resetax, 'Reset', color='lightgoldenrodyellow', hovercolor='0.975')

        # Update function
        def update(val):
            amp = slider_amp.val
            freq = slider_freq.val
            line.set_ydata(amp * np.sin(freq * x))
            fig.canvas.draw_idle()

        # Reset function
        def reset(event):
            slider_amp.reset()
            slider_freq.reset()

        # Connect update function to sliders
        slider_amp.on_changed(update)
        slider_freq.on_changed(update)

        # Connect reset function to button
        button.on_clicked(reset)

        plt.show()
