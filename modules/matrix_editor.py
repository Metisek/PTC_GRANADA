import customtkinter as ctk
import numpy as np
import csv
from tkinter import filedialog, StringVar, messagebox

class MatrixEditorFrame(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.matrix = np.zeros((7, 7))
        self.matrix_rows = 7
        self.matrix_cols = 7
        self.create_widgets()

    def create_widgets(self):
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)
        ctk.CTkButton(button_frame, text="Load Matrix", command=self.load_matrix).grid(row=0, column=0, padx=5)
        ctk.CTkButton(button_frame, text="Save Matrix", command=self.save_matrix).grid(row=0, column=1, padx=5)
        ctk.CTkButton(button_frame, text="Clear Matrix", command=self.clear_matrix).grid(row=0, column=2, padx=5)

        size_frame = ctk.CTkFrame(self)
        size_frame.pack(pady=10)
        ctk.CTkLabel(size_frame, text="Matrix Rows:").grid(row=0, column=0)
        self.rows_var = StringVar(value=str(self.matrix_rows))
        ctk.CTkEntry(size_frame, textvariable=self.rows_var, width=50).grid(row=0, column=1, padx=5)
        ctk.CTkLabel(size_frame, text="Matrix Columns:").grid(row=0, column=2)
        self.cols_var = StringVar(value=str(self.matrix_cols))
        ctk.CTkEntry(size_frame, textvariable=self.cols_var, width=50).grid(row=0, column=3, padx=5)
        ctk.CTkButton(size_frame, text="Update Size", command=self.update_size).grid(row=0, column=4, padx=5)

        action_frame = ctk.CTkFrame(self)
        action_frame.pack(pady=10)
        ctk.CTkButton(action_frame, text="Transpose Matrix", command=self.transpose_matrix).grid(row=0, column=0, padx=5)
        ctk.CTkButton(action_frame, text="Matrix Inverse", command=self.matrix_inverse).grid(row=0, column=1, padx=5)

        self.matrix_frame = ctk.CTkFrame(self)
        self.matrix_frame.pack(pady=10)
        self.entries = [[ctk.CTkEntry(self.matrix_frame, width=60, justify="center") for _ in range(7)] for _ in range(7)]
        for i in range(7):
            for j in range(7):
                self.entries[i][j].grid(row=i, column=j, padx=2, pady=2)

        self.update_display()

    def load_matrix(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("NumPy files", "*.npy")])
        if file_path.endswith(".csv"):
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                data = list(reader)
                self.matrix = np.array([[float(cell) if cell else 0 for cell in row] for row in data])
        elif file_path.endswith(".npy"):
            self.matrix = np.load(file_path)
        self.detect_size()
        self.update_display()

    def save_matrix(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("NumPy files", "*.npy")])
        if file_path.endswith(".csv"):
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(self.matrix[:self.matrix_rows, :self.matrix_cols])
        elif file_path.endswith(".npy"):
            np.save(file_path, self.matrix[:self.matrix_rows, :self.matrix_cols])

    def clear_matrix(self):
        for row in self.entries:
            for entry in row:
                entry.delete(0, ctk.END)

    def detect_size(self):
        rows, cols = self.matrix.shape
        nonzero_rows = np.any(self.matrix != 0, axis=1).sum()
        nonzero_cols = np.any(self.matrix != 0, axis=0).sum()
        self.matrix_rows = nonzero_rows or 1
        self.matrix_cols = nonzero_cols or 1
        self.rows_var.set(str(self.matrix_rows))
        self.cols_var.set(str(self.matrix_cols))

    def update_size(self):
        try:
            rows = int(self.rows_var.get())
            cols = int(self.cols_var.get())
            self.matrix_rows = max(1, min(rows, 7))
            self.matrix_cols = max(1, min(cols, 7))
            self.update_display()
        except ValueError:
            messagebox.showerror("Error", "Invalid matrix size input.")

    def update_display(self):
        for i in range(7):
            for j in range(7):
                self.entries[i][j].delete(0, ctk.END)
                if i < self.matrix_rows and j < self.matrix_cols:
                    value = self.matrix[i, j]
                    if value != 0:
                        self.entries[i][j].insert(0, str(value))

    def update_matrix_from_input(self):
        """Aktualizuje wewnętrzną macierz na podstawie wprowadzonych wartości."""
        for i in range(7):
            for j in range(7):
                value = self.entries[i][j].get()
                self.matrix[i, j] = float(value) if value else 0
        self.detect_size()

    def transpose_matrix(self):
        self.update_matrix_from_input()
        transposed = self.matrix[:self.matrix_rows, :self.matrix_cols].T
        self.matrix[:self.matrix_cols, :self.matrix_rows] = transposed
        self.matrix_rows, self.matrix_cols = self.matrix_cols, self.matrix_rows
        self.update_display()

    def matrix_inverse(self):
        self.update_matrix_from_input()
        if self.matrix_rows != self.matrix_cols:
            messagebox.showerror("Error", "Matrix inverse is only defined for square matrices.")
            return
        try:
            inverted = np.linalg.inv(self.matrix[:self.matrix_rows, :self.matrix_cols])
            self.matrix[:self.matrix_rows, :self.matrix_cols] = inverted
            self.update_display()
        except np.linalg.LinAlgError:
            messagebox.showerror("Error", "Matrix is not invertible.")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.title("Matrix Editor")
    app.geometry("600x600")

    frame = MatrixEditorFrame(app)
    frame.pack(pady=20, padx=20)

    app.mainloop()
