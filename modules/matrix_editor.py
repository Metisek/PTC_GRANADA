import customtkinter as ctk
import numpy as np
import csv
from tkinter import filedialog, StringVar, messagebox

class MatrixEditorFrame(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.matrix = None
        self.submatrix_start = (0, 0)
        self.create_widgets()

    def create_widgets(self):
        # Load and Save buttons
        load_button = ctk.CTkButton(self, text="Load Matrix", command=self.load_matrix)
        load_button.pack(pady=5)
        save_button = ctk.CTkButton(self, text="Save Matrix", command=self.save_matrix)
        save_button.pack(pady=5)

        # Matrix display
        self.matrix_frame = ctk.CTkFrame(self)
        self.matrix_frame.pack(pady=10)

        self.entries = [[ctk.CTkEntry(self.matrix_frame, width=5) for _ in range(7)] for _ in range(7)]
        for i in range(7):
            for j in range(7):
                self.entries[i][j].grid(row=i, column=j, padx=2, pady=2)

        # Navigation
        nav_frame = ctk.CTkFrame(self)
        nav_frame.pack(pady=10)
        ctk.CTkLabel(nav_frame, text="Row:").pack(side="left")
        self.row_var = StringVar(value="0")
        ctk.CTkEntry(nav_frame, textvariable=self.row_var, width=5).pack(side="left")
        ctk.CTkLabel(nav_frame, text="Column:").pack(side="left")
        self.col_var = StringVar(value="0")
        ctk.CTkEntry(nav_frame, textvariable=self.col_var, width=5).pack(side="left")
        ctk.CTkButton(nav_frame, text="Go", command=self.update_submatrix).pack(side="left", padx=5)

        # Transpose and Rotate buttons
        self.transpose_button = ctk.CTkButton(self, text="Transpose", command=self.transpose_matrix)
        self.transpose_button.pack(pady=5)
        self.rotate_button = ctk.CTkButton(self, text="Rotate", command=self.rotate_matrix)
        self.rotate_button.pack(pady=5)

    def load_matrix(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("NumPy files", "*.npy")])
        if file_path.endswith(".csv"):
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                self.matrix = np.array(list(reader)).astype(float)
        elif file_path.endswith(".npy"):
            self.matrix = np.load(file_path)
        self.update_submatrix()

    def save_matrix(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("NumPy files", "*.npy")])
        if file_path.endswith(".csv"):
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(self.matrix)
        elif file_path.endswith(".npy"):
            np.save(file_path, self.matrix)

    def update_submatrix(self):
        try:
            row = int(self.row_var.get())
            col = int(self.col_var.get())
            self.submatrix_start = (row, col)
            submatrix = self.matrix[row:row+7, col:col+7]
            for i in range(7):
                for j in range(7):
                    if i < submatrix.shape[0] and j < submatrix.shape[1]:
                        self.entries[i][j].delete(0, ctk.END)
                        self.entries[i][j].insert(0, str(submatrix[i, j]))
                    else:
                        self.entries[i][j].delete(0, ctk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def transpose_matrix(self):
        self.matrix = self.matrix.T
        self.update_submatrix()

    def rotate_matrix(self):
        if self.matrix.shape[0] == self.matrix.shape[1]:
            self.matrix = np.rot90(self.matrix)
            self.update_submatrix()
        else:
            messagebox.showwarning("Warning", "Rotation is only available for square matrices.")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.title("Matrix Editor")
    app.geometry("600x400")

    frame = MatrixEditorFrame(app)
    frame.pack(pady=20, padx=20)

    app.mainloop()