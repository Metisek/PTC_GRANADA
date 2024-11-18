import ex1
import ex2
import ex3
import ex4
import ex5
import ex6
import ex7
import numpy as np
import tkinter as tk

# Seed as a input argument
seed = 42

# Output file names
ex_3_output_path = "out/ex3_output.gif"

# Function for hanfling turning on exercises
def main():
    root = tk.Tk()
    root.title("Exercise Launcher")

    def run_exercise(exercise):
        exercise.run()

    exercises = [
        ("Exercise 1", ex1.ex1(seed)),
        ("Exercise 2", ex2.ex2()),
        ("Exercise 3", ex3.ex3(ex_3_output_path)),
        ("Exercise 4", ex4.ex4()),
        ("Exercise 5", ex5.ex5()),
        ("Exercise 6", ex6.ex6()),
        ("Exercise 7", ex7.ex7()),
    ]

    for (text, exercise) in exercises:
        button = tk.Button(root, text=text, command=lambda ex=exercise: run_exercise(ex),
                           font=("Helvetica", 14), bg="lightblue", fg="black", padx=20, pady=10)
        button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

