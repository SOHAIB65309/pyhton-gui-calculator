import tkinter as tk

def calculate_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 + num2)
    except ValueError:
        result.set("Invalid input")

def calculate_subtraction():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 - num2)
    except ValueError:
        result.set("Invalid input")
def calculate_mul():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 * num2)
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


label_result_text = tk.Label(root, text="Result:")
label_result_text.pack()

result = tk.StringVar()
label = tk.Label(root, textvariable=result) 
label.pack()
  
button = tk.Button(root, text="Add", command=calculate_sum) 
button.pack()
label_result = tk.Label(root, textvariable=result)
label_result.pack()

button_add = tk.Button(root, text="Add", command=calculate_sum)
button_add.pack()

button_sub = tk.Button(root, text="subtraction", command=calculate_subtraction)
button_sub.pack()
button_sub = tk.Button(root, text="mul", command=calculate_mul)
button_sub.pack()

root.mainloop()
