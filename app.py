import tkinter as tk

def calculate():
    val1 = entry1.get().strip()
    val2 = entry2.get().strip()
    operation = entry_op.get().lower().strip()

    # 1. Check for empty inputs
    if not val1 or not val2:
        result.set("Error: Missing numbers")
        return

    try:
        # 2. Attempt numeric conversion
        num1 = float(val1)
        num2 = float(val2)

        # 3. Logic for operations
        if operation == "add":
            result.set(num1 + num2)
        elif operation == "sub":
            result.set(num1 - num2)
        elif operation == "":
            result.set("Error: Choose an operation")
        else:
            result.set(f"Unknown: '{operation}'")

    except ValueError:
        result.set("Error: Use numbers only")

root = tk.Tk()
root.title("Simple Calculator")


label1 = tk.Label(root, text="Enter 1st Number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter 2nd Number:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label_op = tk.Label(root, text="Enter Operation (add / sub):")
label_op.pack()
entry_op = tk.Entry(root)
entry_op.pack()

label_result_text = tk.Label(root, text="Result:")
label_result_text.pack()

result = tk.StringVar()
label = tk.Label(root, textvariable=result)
label.pack()

button_calc = tk.Button(root, text="Calculate", command=calculate)
button_calc.pack()

root.mainloop()
