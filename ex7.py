from tkinter import Tk, Canvas, Frame, Label, Entry, Button, OptionMenu, StringVar, messagebox
from exercise_class_init import Exercise


class ex7(Exercise):
    def __init__(self):
        super().__init__()

    def solve(self):
        self.root = Tk()
        self.root.title("Shape Drawer")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Canvas for drawing
        self.canvas = Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.pack()

        # Variables for shape and color selection
        self.shape = StringVar(value="Rectangle")
        self.color = StringVar(value="black")

        # Initialize GUI
        self.create_widgets()
        self.bind_shortcuts()

        # Start the main event loop
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.print_result()
            self.root.destroy()

    def create_widgets(self):
        control_frame = Frame(self.root)
        control_frame.pack(pady=10)

        # Shape selection
        Label(control_frame, text="Shape:").grid(row=0, column=0, padx=5, pady=5)
        OptionMenu(control_frame, self.shape, "Rectangle", "Oval", "Line").grid(row=0, column=1, padx=5, pady=5)

        # Color selection
        Label(control_frame, text="Color:").grid(row=0, column=2, padx=5, pady=5)
        OptionMenu(control_frame, self.color, "black", "red", "blue", "green", "yellow").grid(row=0, column=3, padx=5, pady=5)

        # Coordinate inputs
        Label(control_frame, text="x1:").grid(row=1, column=0, padx=5, pady=5)
        self.x1_entry = Entry(control_frame, width=5)
        self.x1_entry.grid(row=1, column=1, padx=5, pady=5)

        Label(control_frame, text="y1:").grid(row=1, column=2, padx=5, pady=5)
        self.y1_entry = Entry(control_frame, width=5)
        self.y1_entry.grid(row=1, column=3, padx=5, pady=5)

        Label(control_frame, text="x2:").grid(row=2, column=0, padx=5, pady=5)
        self.x2_entry = Entry(control_frame, width=5)
        self.x2_entry.grid(row=2, column=1, padx=5, pady=5)

        Label(control_frame, text="y2:").grid(row=2, column=2, padx=5, pady=5)
        self.y2_entry = Entry(control_frame, width=5)
        self.y2_entry.grid(row=2, column=3, padx=5, pady=5)

        # Draw and Clear buttons
        Button(control_frame, text="Draw", command=self.draw_shape, bg="green", fg="white").grid(row=3, column=0, columnspan=2, pady=10)
        Button(control_frame, text="Clear Canvas", command=self.clear_canvas, bg="red", fg="white").grid(row=3, column=2, columnspan=2, pady=10)

    def bind_shortcuts(self):
        # Bind keys for shape selection
        self.root.bind("r", lambda event: self.set_shape("Rectangle"))
        self.root.bind("o", lambda event: self.set_shape("Oval"))
        self.root.bind("l", lambda event: self.set_shape("Line"))
        # Bind key for drawing
        self.root.bind("p", lambda event: self.draw_shape())

    def set_shape(self, shape):
        """Set the shape based on keyboard shortcut."""
        self.shape.set(shape)

    def clear_canvas(self):
        """Clear all shapes from the canvas."""
        self.canvas.delete("all")

    def draw_shape(self):
        """Draw the selected shape on the canvas."""
        try:
            # Parse coordinates
            x1 = int(self.x1_entry.get())
            y1 = int(self.y1_entry.get())
            x2 = int(self.x2_entry.get())
            y2 = int(self.y2_entry.get())
            color = self.color.get()
            shape = self.shape.get()

            # Draw the appropriate shape
            if shape == "Rectangle":
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            elif shape == "Oval":
                self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)
            elif shape == "Line":
                self.canvas.create_line(x1, y1, x2, y2, fill=color)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid integer coordinates.")
