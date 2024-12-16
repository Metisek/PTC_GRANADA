import customtkinter as ctk
from tkinter import messagebox, Listbox, END
import random

class GuessNumberFrame(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.random_number = random.randint(0, 100)
        self.guess_history = []

        self.create_ui()

    def create_ui(self):
        # Entry for input
        self.entry = ctk.CTkEntry(self, font=("Arial", 24), width=200, placeholder_text="0-100")
        self.entry.pack(pady=10)

        # Button to check the guess
        check_button = ctk.CTkButton(self, text="Verify", command=self.check_guess)
        check_button.pack(pady=5)

        # Label for feedback
        self.feedback_label = ctk.CTkLabel(self, text="", font=("Arial", 16))
        self.feedback_label.pack(pady=5)

        # Listbox for history of attempts
        self.history_listbox = Listbox(self, height=10, width=30)
        self.history_listbox.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < 0 or guess > 100:
                self.feedback_label.configure(text="Please enter a number between 0 and 100.")
                return

            # Update history
            self.guess_history.append(guess)
            self.history_listbox.insert(END, f"Attempt: {guess}")

            # Check the guess
            if guess < self.random_number:
                self.feedback_label.configure(text="The number is larger.")
            elif guess > self.random_number:
                self.feedback_label.configure(text="The number is smaller.")
            else:
                messagebox.showinfo("Congratulations!", "You've guessed the number!")
                self.reset_game()
        except ValueError:
            self.feedback_label.configure(text="Invalid input. Please enter an integer.")

    def reset_game(self):
        self.random_number = random.randint(0, 100)
        self.guess_history.clear()
        self.history_listbox.delete(0, END)
        self.entry.delete(0, END)
        self.feedback_label.configure(text="")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.title("Guess the Number")
    app.geometry("400x400")

    frame = GuessNumberFrame(app)
    frame.pack(expand=True, padx=20, pady=20)

    app.mainloop()
