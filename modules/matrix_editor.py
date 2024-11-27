import customtkinter as ctk
import numpy as np
import csv
from tkinter import filedialog, StringVar, messagebox

class MatrixEditorFrame(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.matrix = None
        self.matrix_rows = 0
        self.matrix_cols = 0
        self.center_x = 4
        self.center_y = 4
        self.create_widgets()

    def create_widgets(self):
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)
        ctk.CTkButton(button_frame, text="Load Matrix", command=self.load_matrix).grid(row=0, column=0, padx=5)
        self.save_button = ctk.CTkButton(button_frame, text="Save Matrix", command=self.save_matrix, state="disabled")
        self.save_button.grid(row=0, column=1, padx=5)
        ctk.CTkButton(button_frame, text="Clear Matrix", command=self.clear_matrix).grid(row=0, column=2, padx=5)

        coord_frame = ctk.CTkFrame(self)
        coord_frame.pack(pady=10)
        ctk.CTkLabel(coord_frame, text="Center X:").grid(row=0, column=0)
        self.center_x_var = StringVar(value=str(self.center_x))
        ctk.CTkEntry(coord_frame, textvariable=self.center_x_var, width=50).grid(row=0, column=1, padx=5)
        ctk.CTkLabel(coord_frame, text="Center Y:").grid(row=0, column=2)
        self.center_y_var = StringVar(value=str(self.center_y))
        ctk.CTkEntry(coord_frame, textvariable=self.center_y_var, width=50).grid(row=0, column=3, padx=5)
        ctk.CTkButton(coord_frame, text="Update Center", command=self.update_center).grid(row=0, column=4, padx=5)

        action_frame = ctk.CTkFrame(self)
        action_frame.pack(pady=10)
        self.transpose_button = ctk.CTkButton(action_frame, text="Transpose Matrix", command=self.transpose_matrix, state="disabled")
        self.transpose_button.grid(row=0, column=0, padx=5)
        self.inverse_button = ctk.CTkButton(action_frame, text="Matrix Inverse", command=self.matrix_inverse, state="disabled")
        self.inverse_button.grid(row=0, column=1, padx=5)

        self.matrix_frame = ctk.CTkFrame(self)
        self.matrix_frame.pack(pady=10)
        self.entries = [[ctk.CTkEntry(self.matrix_frame, width=60, justify="center") for _ in range(7)] for _ in range(7)]
        for i in range(7):
            for j in range(7):
                self.entries[i][j].grid(row=i, column=j, padx=2, pady=2)
        for row in self.entries:
            for entry in row:
                entry.bind("<FocusOut>", self.validate_and_update_matrix)

        self.info_label = ctk.CTkLabel(self, text="Matrix currently undefined")
        self.info_label.pack(pady=10)

        self.update_display()

    def validate_and_update_matrix(self, event):
        entry = event.widget
        value = entry.get()
        if value:
            try:
                float(value)
                self.load_matrix_from_input()
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Only numeric values are allowed.")
                entry.delete(0, ctk.END)

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
        self.matrix = None
        self.matrix_rows = 0
        self.matrix_cols = 0
        self.update_display()

    def detect_size(self):
        if self.matrix is not None:
            rows, cols = self.matrix.shape
            self.matrix_rows = rows
            self.matrix_cols = cols
        else:
            self.matrix_rows = 0
            self.matrix_cols = 0
        self.update_info_label()

    def update_size(self):
        try:
            rows = int(self.rows_var.get())
            cols = int(self.cols_var.get())
            self.matrix_rows = max(1, rows)
            self.matrix_cols = max(1, cols)
            if self.matrix is None:
                self.matrix = np.zeros((self.matrix_rows, self.matrix_cols))
            else:
                self.matrix = np.resize(self.matrix, (self.matrix_rows, self.matrix_cols))
            self.update_display()
        except ValueError:
            messagebox.showerror("Error", "Invalid matrix size input.")

    def update_center(self):
        try:
            self.center_x = int(self.center_x_var.get())
            self.center_y = int(self.center_y_var.get())
            self.update_display()
        except ValueError:
            messagebox.showerror("Error", "Invalid center coordinates input.")

    def update_display(self):
        start_row = max(0, self.center_y - 4)
        start_col = max(0, self.center_x - 4)
        end_row = min(self.matrix_rows, start_row + 7)
        end_col = min(self.matrix_cols, start_col + 7)

        for i in range(7):
            for j in range(7):
                self.entries[i][j].delete(0, ctk.END)
                if self.matrix is not None and start_row + i < end_row and start_col + j < end_col:
                    value = self.matrix[start_row + i, start_col + j]
                    if value != 0:
                        self.entries[i][j].insert(0, str(value))

        self.update_info_label()

    def load_matrix_from_input(self):
        start_row = max(0, self.center_y - 4)
        start_col = max(0, self.center_x - 4)
        current_max_row = 0
        current_max_col = 0
        new_matrix = np.zeros((start_row + 7, start_col + 7))
        for i in range(6, -1, -1):
            for j in range(6, -1, -1):
                value = self.entries[i][j].get()
                if value:
                    if value != '0':
                        new_matrix[start_row + i, start_col + j] = float(value)
                        current_max_row = max(current_max_row, start_row + i + 1)
                        current_max_col = max(current_max_col, start_col + j + 1)

        if self.matrix is None:
            # Remove zero rows and columns from bottom and right sides
            non_zero_rows = np.any(new_matrix != 0, axis=1)
            non_zero_cols = np.any(new_matrix != 0, axis=0)
            last_non_zero_row = np.where(non_zero_rows)[0][-1] + 1 if np.any(non_zero_rows) else 0
            last_non_zero_col = np.where(non_zero_cols)[0][-1] + 1 if np.any(non_zero_cols) else 0
            new_matrix = new_matrix[:last_non_zero_row, :last_non_zero_col]
            self.matrix = new_matrix
        else:
            max_rows = max(self.matrix.shape[0], new_matrix.shape[0])
            max_cols = max(self.matrix.shape[1], new_matrix.shape[1])
            resized_matrix = np.zeros((max_rows, max_cols))
            resized_matrix[:self.matrix.shape[0], :self.matrix.shape[1]] = self.matrix
            for i in range(new_matrix.shape[0]):
                for j in range(new_matrix.shape[1]):
                    if start_row + i < max_rows and start_col + j < max_cols:
                        resized_matrix[start_row + i, start_col + j] = new_matrix[i, j]
            # Remove zero rows and columns from bottom and right sides
            non_zero_rows = np.any(resized_matrix != 0, axis=1)
            non_zero_cols = np.any(resized_matrix != 0, axis=0)
            last_non_zero_row = np.where(non_zero_rows)[0][-1] + 1 if np.any(non_zero_rows) else 0
            last_non_zero_col = np.where(non_zero_cols)[0][-1] + 1 if np.any(non_zero_cols) else 0
            resized_matrix = resized_matrix[:last_non_zero_row, :last_non_zero_col]
            self.matrix = resized_matrix

        for i in range(7):
            for j in range(7):
                value = self.entries[i][j].get()
                if not value and i + start_row < current_max_row and j + start_col < current_max_col:
                    self.entries[i][j].insert(0, "0")
                    new_matrix[start_row + i, start_col + j] = 0
                elif i + start_row >= current_max_row or j + start_row >= current_max_col:
                    self.entries[i][j].delete(0, ctk.END)

        self.detect_size()
        self.update_info_label()
        self.transpose_button.configure(state="normal")
        self.inverse_button.configure(state="normal")
        self.save_button.configure(state="normal")

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

    def update_info_label(self):
        if self.matrix is None:
            self.info_label.configure(text="Matrix currently undefined")
        else:
            self.info_label.configure(text=f"Matrix size: {self.matrix_rows}x{self.matrix_cols}")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.title("Matrix Editor")
    app.geometry("600x600")

    frame = MatrixEditorFrame(app)
    frame.pack(pady=20, padx=20)

    app.mainloop()