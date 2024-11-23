import os
import sys
import customtkinter as ctk
from tkinter import Tk
from sympy import sympify
from modules.symbolic_calculator import SymbolicCalculatorFrame
from modules.dynamic_chart import DynamicChartFrame
from modules.history import HistoryFrame
from modules.apply_csv import ApplyCSV
from modules.matrix_editor import MatrixEditorFrame

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
    tab_view.add("History")
    tab_view.add("Apply CSV")
    tab_view.add("Matrix Editor")

    # Inicjalizacja zawartości zakładek
    def load_symbolic_calculator_tab():
        global symbolic_calculator_frame
        symbolic_calculator_frame = SymbolicCalculatorFrame(tab_view.tab("Symbolic Calculator"))
        symbolic_calculator_frame.pack(fill="both", expand=True)
        symbolic_calculator_frame.result_var.trace_add("write", update_dynamic_chart)
        symbolic_calculator_frame.result_var.trace_add("write", update_history)

    def load_dynamic_chart_tab():
        global dynamic_chart_frame
        dynamic_chart_frame = DynamicChartFrame(tab_view.tab("Dynamic Chart"), expression=last_expression, is_independent=False)
        dynamic_chart_frame.pack(fill="both", expand=True)

    def load_history_tab():
        global history_frame
        history_frame = HistoryFrame(tab_view.tab("History"), symbolic_calculator_frame)
        history_frame.pack(fill="both", expand=True)

    def load_apply_csv_tab():
        apply_csv_frame = ApplyCSV(tab_view.tab("Apply CSV"), symbolic_calculator_frame)
        apply_csv_frame.pack(fill="both", expand=True)

    def load_matrix_editor_tab():
        matrix_editor_frame = MatrixEditorFrame(tab_view.tab("Matrix Editor"))
        matrix_editor_frame.pack(fill="both", expand=True)

    def update_dynamic_chart(*args):
        global last_expression
        if symbolic_calculator_frame and dynamic_chart_frame:
            last_expression = sympify(symbolic_calculator_frame.result_var.get())
            dynamic_chart_frame.update_expression(last_expression)

    def update_history(*args):
        if symbolic_calculator_frame and history_frame:
            expression = symbolic_calculator_frame.input_field.get()
            result = symbolic_calculator_frame.result_var.get()
            history_frame.add_history(expression, result)

    load_symbolic_calculator_tab()
    load_dynamic_chart_tab()
    load_history_tab()
    load_apply_csv_tab()
    load_matrix_editor_tab()

    # Główna pętla aplikacji
    root.mainloop()

if __name__ == "__main__":
    main()