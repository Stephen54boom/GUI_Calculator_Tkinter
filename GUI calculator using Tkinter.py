import tkinter as tk

def button_click(symbol):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + symbol)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the display
display = tk.Entry(root, width=20, font=('Arial', 20), borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, padx=20, pady=10, font=('Arial', 16), command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text='C', padx=20, pady=10, font=('Arial', 16), command=clear)
clear_btn.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Calculate button
calculate_btn = tk.Button(root, text='=', padx=20, pady=10, font=('Arial', 16), command=calculate)
calculate_btn.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
