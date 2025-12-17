import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = entry_op.get().lower()

        if operation == "add":
            result.set(num1 + num2)
        elif operation == "sub":
            result.set(num1 - num2)
        else:
            result.set("Invalid operation")
    except ValueError:
        result.set("Invalid input")

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
