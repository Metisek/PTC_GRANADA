import customtkinter as ctk

class CounterFrame(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        # Counter value
        self.counter = ctk.DoubleVar(value=0.0)

        # Create UI
        self.create_ui()

    def create_ui(self):
        # Main frame for centering
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(expand=True)

        # Entry widget for displaying/modifying counter
        self.entry = ctk.CTkEntry(main_frame,
                                 textvariable=self.counter,
                                 font=("Arial", 24),
                                 justify="center",
                                 width=100)
        self.entry.pack(pady=10)
        self.entry.bind("<Double-1>", self.reset_counter)  # Bind double-click event

        # Increase and Decrease Buttons
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack()

        increase_button = ctk.CTkButton(button_frame,
                                        text="Increase",
                                        command=self.increase_counter,
                                        font=("Arial", 14))
        increase_button.pack(side="left", padx=10)

        decrease_button = ctk.CTkButton(button_frame,
                                        text="Decrease",
                                        command=self.decrease_counter,
                                        font=("Arial", 14))
        decrease_button.pack(side="right", padx=10)

    # Button functions
    def increase_counter(self):
        try:
            self.counter.set(self.counter.get() + 1)
        except ValueError:
            self.counter.set(0)  # Handle invalid inputs

    def decrease_counter(self):
        try:
            self.counter.set(self.counter.get() - 1)
        except ValueError:
            self.counter.set(0)  # Handle invalid inputs

    # Reset function for double-click
    def reset_counter(self, event):
        self.counter.set(0.0)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.title("Counter")
    app.geometry("800x600")

    frame = CounterFrame(app)
    frame.pack(expand=True)

    app.mainloop()
