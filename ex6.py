from exercise_class_init import Exercise
import tkinter as tk
from tkinter import messagebox

class ex6(Exercise):
    def __init__(self):
        super().__init__()

    def solve(self):
        def update_label():
            text = entry.get()
            if not text:
                messagebox.showwarning("Warning", "The entry field is empty!")
            else:
                result_label.config(text=f"You entered: {text}", fg="green")


        def exit_app():
            root.destroy()
            self.print_result()

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.print_result()
                root.destroy()




        # Initialize the main application window
        root = tk.Tk()
        root.title("Label Update with Tkinter")
        root.protocol("WM_DELETE_WINDOW", on_closing)

        # Create and place the main label
        main_label = tk.Label(root, text="Write something and press 'Submit':")
        main_label.pack(pady=10)

        # Create and place the entry field
        entry = tk.Entry(root, width=40)
        entry.pack(pady=5)

        # Create and place the buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        submit_button = tk.Button(
            button_frame, text="Submit", bg="#ADD8E6", fg="black", width=10, command=update_label
        )
        submit_button.grid(row=0, column=0, padx=5)

        exit_button = tk.Button(
            button_frame, text="Exit", bg="#FF6347", fg="black", width=10, command=exit_app
        )
        exit_button.grid(row=0, column=1, padx=5)

        # Create and place the result label
        result_label = tk.Label(root, text="", font=("Arial", 10), fg="green")
        result_label.pack(pady=10)


        # Start the Tkinter event loop
        root.mainloop()