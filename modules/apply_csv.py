# modules/apply_csv.py
import pandas as pd
import customtkinter as ctk
from tkinter import filedialog, messagebox, simpledialog, ttk
from sympy import sympify

class ApplyCSV(ctk.CTkFrame):
    def __init__(self, parent, symbolic_calculator_frame):
        super().__init__(parent)
        self.symbolic_calculator_frame = symbolic_calculator_frame
        self.data = None

        self.load_button = ctk.CTkButton(self, text="Load CSV", command=self.load_csv)
        self.load_button.pack(pady=5)

        self.apply_button = ctk.CTkButton(self, text="Apply Equation", command=self.apply_equation)
        self.apply_button.pack(pady=5)

        self.save_button = ctk.CTkButton(self, text="Save CSV", command=self.save_csv)
        self.save_button.pack(pady=5)

        self.tree = ttk.Treeview(self)
        self.tree.pack(fill="both", expand=True, pady=5)

        self.tree.bind("<Double-1>", self.on_double_click)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        try:
            self.data = pd.read_csv(file_path, delimiter=",", encoding="utf-8")

            if not all(col in self.data.columns for col in ['x', 'y', 'z']):
                self.data = pd.read_csv(file_path, delimiter=";", encoding="utf-8")

                if all(col in self.data.columns for col in ['x', 'y', 'z']):
                    messagebox.showinfo(
                        "Notice",
                        "The file appears to use ';' as a delimiter (likely from Excel). Data was successfully loaded."
                    )
                else:
                    raise ValueError("CSV file must contain columns 'x', 'y', and 'z'.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {e}")
            return

        self.data = self.data[['x', 'y', 'z']].fillna('')
        self.check_and_replace_non_numeric()
        self.update_treeview()



    def check_and_replace_non_numeric(self):
        non_numeric_found = False
        for column in ['x', 'y', 'z']:
            if column in self.data.columns:
                for index, value in self.data[column].items():
                    try:
                        self.data.at[index, column] = float(value)
                    except (ValueError, TypeError):
                        self.data.at[index, column] = 0
                        non_numeric_found = True
        if non_numeric_found:
            messagebox.showwarning("Warning", "Non-numeric, empty, or NaN values detected and replaced with 0.")

    def apply_equation(self):
        if self.data is not None:
            expression = sympify(self.symbolic_calculator_frame.result_var.get())
            column_name = str(expression)
            if len(self.data.columns) > 3:
                self.data = self.data[['x', 'y', 'z']]  # Keep only x, y, z columns
            self.data[column_name] = self.data.apply(lambda row: expression.evalf(subs={'x': row['x'], 'y': row['y'], 'z': row['z']}), axis=1)
            self.update_treeview()

    def save_csv(self):
        if self.data is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if file_path:
                self.data.to_csv(file_path, index=False)

    def update_treeview(self):
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(self.data.columns)
        self.tree["show"] = "headings"
        for column in self.tree["columns"]:
            self.tree.heading(column, text=column, command=lambda _col=column: self.sort_by(_col, False))
        for _, row in self.data.iterrows():
            self.tree.insert("", "end", values=list(row))

    def sort_by(self, col, descending):
        data_list = [(self.tree.set(child, col), child) for child in self.tree.get_children('')]
        data_list.sort(reverse=descending)
        for index, (val, child) in enumerate(data_list):
            self.tree.move(child, '', index)
        self.tree.heading(col, command=lambda: self.sort_by(col, not descending))

    def on_double_click(self, event):
        try:
            item = self.tree.selection()[0]
            column = self.tree.identify_column(event.x)
            column_index = int(column.replace('#', '')) - 1

            column_name = self.tree["columns"][column_index]
            row_index = int(self.tree.index(item))
            value = self.data.iloc[row_index, column_index]

            new_value = simpledialog.askstring(
                "Input",
                f"Modify value for {column_name}",
                initialvalue=value
            )

            if new_value:
                try:
                    new_value = float(new_value)
                except ValueError:
                    new_value = 0
                    messagebox.showwarning(
                        "Warning",
                        f"Non-numeric value detected for column '{column_name}'. Replaced with 0."
                    )

                self.data.at[row_index, column_name] = new_value
                self.update_treeview()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    messagebox.showwarning("Warning", "This module should be run from main.py")