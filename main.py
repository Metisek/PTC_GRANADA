import os
import sys
import customtkinter as ctk
from tkinter import Tk
from sympy import sympify
from modules.symbolic_calculator import SymbolicCalculatorFrame
from modules.dynamic_chart import DynamicChartFrame

last_expression = None

def main():
    global last_expression

    # Inicjalizacja okna głównego aplikacji
    root = Tk()
    root.title("Modular Application")
    root.geometry("1000x700")

    # CustomTkinter style
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    # Tworzenie TabView do zarządzania zakładkami
    tab_view = ctk.CTkTabview(root)
    tab_view.pack(fill="both", expand=True, padx=10, pady=10)

    # Dodawanie zakładek
    tab_view.add("Symbolic Calculator")
    tab_view.add("Dynamic Chart")
    tab_view.add("Module 3")

    # Inicjalizacja zawartości zakładek
    def load_symbolic_calculator_tab():
        global symbolic_calculator_frame
        symbolic_calculator_frame = SymbolicCalculatorFrame(tab_view.tab("Symbolic Calculator"))
        symbolic_calculator_frame.pack(fill="both", expand=True)
        symbolic_calculator_frame.result_var.trace_add("write", update_dynamic_chart)

    def load_dynamic_chart_tab():
        global dynamic_chart_frame
        dynamic_chart_frame = DynamicChartFrame(tab_view.tab("Dynamic Chart"), expression=last_expression, is_independent=False)
        dynamic_chart_frame.pack(fill="both", expand=True)

    def update_dynamic_chart(*args):
        global last_expression
        if symbolic_calculator_frame and dynamic_chart_frame:
            last_expression = sympify(symbolic_calculator_frame.result_var.get())
            dynamic_chart_frame.update_expression(last_expression)

    load_symbolic_calculator_tab()
    load_dynamic_chart_tab()

    # Główna pętla aplikacji
    root.mainloop()


if __name__ == "__main__":
    main()