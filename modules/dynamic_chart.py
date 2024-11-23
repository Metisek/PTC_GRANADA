import customtkinter as ctk
from sympy import symbols, sympify, lambdify
from tkinter import StringVar, Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import re

class DynamicChartFrame(ctk.CTkFrame):
    def __init__(self, master, expression=None, is_independent=False, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.expression = expression
        self.result_var = StringVar()
        self._is_independent = is_independent

        if self._is_independent:
            self.create_input_interface()
        self.create_plot_interface()

        if isinstance(self.master, (Tk, ctk.CTk)):
            self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_input_interface(self):
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(pady=10)

        vcmd = (self.register(self.validate_input), '%P')
        self.input_field = ctk.CTkEntry(input_frame, placeholder_text="Enter expression...", width=600, validate="key", validatecommand=vcmd)
        self.input_field.pack(side="left", padx=5)

        submit_button = ctk.CTkButton(input_frame, text="Submit", fg_color="purple", text_color="white", command=self.submit_expression)
        submit_button.pack(side="right", padx=5)

    def create_notification_interface(self, message):
        notification_label = ctk.CTkLabel(self, text=message, font=("Arial", 16))
        notification_label.pack(pady=10)

    def create_plot_interface(self):
        if self.expression is None and not self._is_independent:
            self.create_notification_interface("Please use the Symbolic Calculator to enter an expression.")
            return

        symbols_in_expr = list(self.expression.free_symbols) if self.expression else []
        num_symbols = len(symbols_in_expr)

        if num_symbols == 0:
            self.result_var.set("Cannot create a plot for constant values.")
            result_label = ctk.CTkLabel(self, textvariable=self.result_var, font=("Arial", 16))
            result_label.pack(pady=10)
        elif num_symbols == 3:
            self.result_var.set("Cannot create a plot for expressions with 3 symbols.")
            result_label = ctk.CTkLabel(self, textvariable=self.result_var, font=("Arial", 16))
            result_label.pack(pady=10)
        elif num_symbols == 2:
            self.create_3d_plot(symbols_in_expr)
        elif num_symbols == 1:
            self.create_2d_plot(symbols_in_expr[0])

    def create_3d_plot(self, symbols_in_expr):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x, y = symbols_in_expr
        x_vals = np.linspace(-5, 5, 50)
        y_vals = np.linspace(-5, 5, 50)
        x_vals, y_vals = np.meshgrid(x_vals, y_vals)
        z_func = lambdify((x, y), self.expression, 'numpy')
        z_vals = z_func(x_vals, y_vals)

        surf = ax.plot_surface(x_vals, y_vals, z_vals, cmap='viridis')
        fig.colorbar(surf)

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack(fill='both', expand=True)

        slider_frame = ctk.CTkFrame(self)
        slider_frame.pack(pady=10)

        elevation_slider = ctk.CTkSlider(slider_frame, from_=0, to=90, command=lambda val: self.update_view(ax, canvas, elev=val))
        elevation_slider.pack(side='left', padx=5)
        azimuth_slider = ctk.CTkSlider(slider_frame, from_=0, to=360, command=lambda val: self.update_view(ax, canvas, azim=val))
        azimuth_slider.pack(side='right', padx=5)

    def create_2d_plot(self, symbol):
        fig, ax = plt.subplots()

        x_vals = np.linspace(-10, 10, 50)
        y_func = lambdify(symbol, self.expression, 'numpy')
        y_vals = y_func(x_vals)

        ax.plot(x_vals, y_vals)
        ax.set_xlabel(str(symbol))
        ax.set_ylabel('f({})'.format(symbol))

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().pack(fill='both', expand=True)

        def on_move(event):
            if event.inaxes:
                x, y = event.xdata, event.ydata
                self.result_var.set(f"x: {x:.2f}, y: {y:.2f}")

        fig.canvas.mpl_connect('motion_notify_event', on_move)
        result_label = ctk.CTkLabel(self, textvariable=self.result_var, font=("Arial", 16))
        result_label.pack(pady=10)

    def update_view(self, ax, canvas, elev=None, azim=None):
        if elev is not None:
            ax.view_init(elev=elev)
        if azim is not None:
            ax.view_init(azim=azim)
        canvas.draw()

    def submit_expression(self):
        expression = self.input_field.get()
        if self.validate_input(expression):
            self.expression = sympify(expression)
            for widget in self.winfo_children():
                widget.destroy()
            self.create_input_interface()
            self.create_plot_interface()

    def update_expression(self, new_expression):
        self.expression = new_expression
        for widget in self.winfo_children():
            widget.destroy()
        self.create_plot_interface()

    def validate_input(self, new_value):
        valid_chars = "0123456789+-*/().^xyz√"
        for char in new_value:
            if char not in valid_chars:
                return False
        return True

    def on_closing(self):
        self.master.quit()
        self.master.destroy()


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.title("Dynamic Chart")
    app.geometry("800x600")

    frame = DynamicChartFrame(app, is_independent=True)
    frame.pack(pady=20, padx=20)

    app.mainloop()