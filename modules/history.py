import customtkinter as ctk
from tkinter import Listbox, END, Tk

class HistoryFrame(ctk.CTkFrame):
    def __init__(self, master, symbolic_calculator_frame=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.symbolic_calculator_frame = symbolic_calculator_frame
        self.history_listbox = Listbox(self)
        self.history_listbox.pack(fill="both", expand=True)
        self.history_listbox.bind('<Double-1>', self.on_double_click)
        self.history = []

        if symbolic_calculator_frame is None:
            self.create_notification_interface("History does not work standalone, only as a tab in the main application.")

    def add_history(self, expression, result):
        entry = f"{expression} -> {result}"
        self.history.append(entry)
        self.history_listbox.insert(END, entry)

    def on_double_click(self, event):
        selection = self.history_listbox.curselection()
        if selection:
            index = selection[0]
            entry = self.history[index]
            expression, result = entry.split(" -> ")
            self.load_expression(expression, result)
            # Usunięcie najnowszego wpisu z historii
            self.history.pop()
            self.history_listbox.delete(END)

    def load_expression(self, expression, result):
        if self.symbolic_calculator_frame:
            self.symbolic_calculator_frame.input_field.delete(0, END)
            self.symbolic_calculator_frame.input_field.insert(0, expression)
            self.symbolic_calculator_frame.result_var.set(result)

    def create_notification_interface(self, message):
        notification_label = ctk.CTkLabel(self, text=message, font=("Arial", 16))
        notification_label.pack(pady=10)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.title("History")
    app.geometry("800x600")

    frame = HistoryFrame(app)
    frame.pack(pady=20, padx=20)

    app.mainloop()