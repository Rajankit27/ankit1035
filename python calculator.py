import tkinter as tk
import math

def calculate_factorial():
    try:
        num = int(entry.get())
        if num < 0:
            result_label.config(text="Factorial is undefined for negative numbers.")
        else:
            result = math.factorial(num)
            result_label.config(text=f"The factorial of {num} is {result}.")
    except ValueError:
        result_label.config(text="Invalid Input.")

# Create main window
window = tk.Tk()
window.minsize(300, 200)
window.title("Factorial Calculator")

# Create input label and entry
label = tk.Label(window, text="Enter a number:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create button to calculate factorial
button = tk.Button(window, text="Calculate", command=calculate_factorial)
button.pack()

# Create result label
result_label = tk.Label(window, text="")
result_label.pack()

# Run the main loop
window.mainloop()