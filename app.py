import tkinter as tk

def calculate_sum():
  try:
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.set(num1 + num2)
  except ValueError:
    result.set("Invalid input")

root = tk.Tk() 
root.title("Simple Calculator")

entry1 = tk.Entry(root) 
entry1.pack()

entry2 = tk.Entry(root) 
entry2.pack()

result = tk.StringVar()
label = tk.Label(root, textvariable=result) 
label.pack()
  
button = tk.Button(root, text="Add", command=calculate_sum) 
button.pack()

root.mainloop()