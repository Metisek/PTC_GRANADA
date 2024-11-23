import customtkinter as ctk
from sympy import symbols, sympify, simplify, diff, integrate, sqrt
from tkinter import StringVar
from tkinter.ttk import Combobox
import re


class SymbolicCalculatorFrame(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Zmienne symboliczne
        self.x, self.y, self.z = symbols("x y z")
        self.result_var = StringVar()

        # Nagłówek
        header_label = ctk.CTkLabel(self, text="Symbolic Calculator", font=("Arial", 20))
        header_label.pack(pady=10)

        # Sekcja Entry
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(pady=10)

        vcmd = (self.register(self.validate_input), '%P')
        self.input_field = ctk.CTkEntry(input_frame, placeholder_text="Enter expression...", width=600, validate="key", validatecommand=vcmd)
        self.input_field.pack(side="left", padx=5)

        clear_button = ctk.CTkButton(input_frame, text="Clear", fg_color="purple", text_color="white",
                                     command=self.clear_input)
        clear_button.pack(side="right", padx=5)

        # Sekcja wyboru zmiennej
        var_frame = ctk.CTkFrame(self)
        var_frame.pack(pady=10)

        var_label = ctk.CTkLabel(var_frame, text="Select Variable:", font=("Arial", 14))
        var_label.pack(side="left", padx=5)

        self.variable_combobox = Combobox(var_frame, values=["x", "y", "z"], state="readonly", width=10)
        self.variable_combobox.current(0)  # Domyślny wybór: x
        self.variable_combobox.pack(side="right", padx=5)

        # Sekcja przycisków operacji
        operations_frame = ctk.CTkFrame(self)
        operations_frame.pack(pady=20)

        self.create_buttons(operations_frame)

        simplify_button = ctk.CTkButton(operations_frame, text="Simplify", fg_color="purple", text_color="white",
                                        command=self.simplify_expression)
        simplify_button.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

        derive_button = ctk.CTkButton(operations_frame, text="Derive", fg_color="purple", text_color="white",
                                      command=self.derive_expression)
        derive_button.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

        integrate_button = ctk.CTkButton(operations_frame, text="Integrate", fg_color="purple", text_color="white",
                                         command=self.integrate_expression)
        integrate_button.grid(row=5, column=4, padx=5, pady=5, columnspan=2)

        # Sekcja wyniku
        result_frame = ctk.CTkFrame(self)
        result_frame.pack(pady=10)

        result_label = ctk.CTkLabel(result_frame, text="Result:", font=("Arial", 16))
        result_label.pack()

        result_display = ctk.CTkLabel(result_frame, textvariable=self.result_var, font=("Arial", 14),
                                      width=600, height=40, anchor="center")
        result_display.pack(pady=5)

    def create_buttons(self, frame):
        """Tworzenie przycisków numerycznych i operatorów."""
        buttons = [
            ("1",), ("2",), ("3",), ("+",), ("-"),
            ("4",), ("5",), ("6",), ("*",), ("/",),
            ("7",), ("8",), ("9",), ("(",), (")",),
            ("0",), (".",), ("^",), ("√",), ("x",),
            ("y",), ("z",)
        ]
        for i, (label,) in enumerate(buttons):
            btn = ctk.CTkButton(frame, text=label, width=50, fg_color="purple", text_color="white",
                                command=lambda b=label: self.append_to_input(b))
            btn.grid(row=i // 5, column=i % 5, padx=5, pady=5)

    def append_to_input(self, value):
        """Dodanie wartości do pola Entry."""
        current_text = self.input_field.get()
        if value == "√":
            value = "^(1/2)"
        self.input_field.delete(0, ctk.END)
        self.input_field.insert(0, current_text + value)

    def clear_input(self):
        """Wyczyszczenie pola Entry."""
        self.input_field.delete(0, ctk.END)

    def insert_multiplication_operators(self, expression):
        """Wstawianie brakujących operatorów mnożenia."""
        expression = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expression)
        expression = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expression)
        expression = re.sub(r'([a-zA-Z])([a-zA-Z])', r'\1*\2', expression)
        expression = re.sub(r'(\))(\()', r'\1*\2', expression)
        expression = re.sub(r'(\))([a-zA-Z])', r'\1*\2', expression)
        expression = re.sub(r'([a-zA-Z])(\()', r'\1*\2', expression)
        return expression

    def validate_input(self, new_value):
        """Walidacja wejściowego tekstu."""
        valid_chars = "0123456789+-*/().^xyz√"
        for char in new_value:
            if char not in valid_chars:
                return False
        return True

    def simplify_expression(self):
        """Uproszczenie wyrażenia."""
        try:
            expression = self.insert_multiplication_operators(self.input_field.get())
            expression = sympify(expression)
            self.result_var.set(str(simplify(expression)))
        except Exception as e:
            self.log_error("Simplify", e)
            self.result_var.set(f"Error: {e}")

    def derive_expression(self):
        """Różniczkowanie wyrażenia."""
        try:
            expression = self.insert_multiplication_operators(self.input_field.get())
            expression = sympify(expression)
            variable = symbols(self.variable_combobox.get())
            self.result_var.set(str(diff(expression, variable)))
        except Exception as e:
            self.log_error("Derive", e)
            self.result_var.set(f"Error: {e}")

    def integrate_expression(self):
        """Całkowanie wyrażenia."""
        try:
            expression = self.insert_multiplication_operators(self.input_field.get())
            expression = sympify(expression)
            variable = symbols(self.variable_combobox.get())
            self.result_var.set(str(integrate(expression, variable)))
        except Exception as e:
            self.log_error("Integrate", e)
            self.result_var.set(f"Error: {e}")

    def log_error(self, operation, error):
        """Zapis błędu w terminalu."""
        print(f"[Error in {operation}]: {error}")


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.title("Symbolic Calculator")
    app.geometry("800x600")

    frame = SymbolicCalculatorFrame(app)
    frame.pack(pady=20, padx=20)

    app.mainloop()