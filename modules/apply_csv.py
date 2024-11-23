# modules/apply_csv.py
import pandas as pd
import customtkinter as ctk
from tkinter import filedialog, messagebox, simpledialog
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

        self.tree = ctk.CTkTreeview(self)
        self.tree.pack(fill="both", expand=True, pady=5)

        self.tree.bind("<Double-1>", self.on_double_click)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.data = pd.read_csv(file_path)
            self.update_treeview()

    def apply_equation(self):
        if self.data is not None:
            expression = sympify(self.symbolic_calculator_frame.result_var.get())
            self.data['result'] = self.data.apply(lambda row: expression.evalf(subs={'x': row['x'], 'y': row['y'], 'z': row['z']}), axis=1)
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
        item = self.tree.selection()[0]
        column = self.tree.identify_column(event.x)
        column_index = int(column.replace('#', '')) - 1
        value = self.tree.item(item, "values")[column_index]
        new_value = simpledialog.askstring("Input", f"Modify value for {self.tree.heading(column)['text']}", initialvalue=value)
        if new_value:
            self.data.at[int(item), self.tree.heading(column)['text']] = new_value
            self.update_treeview()

if __name__ != "__main__":
    messagebox.showwarning("Warning", "This module should be run from main.py")