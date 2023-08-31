'''
info : this file for displaying factorial number
Name : Hossam Adel Mostafa 

'''

import tkinter as tk

def factorial():
    n = int(entry.get())
    fact = math.factorial(n)
    result.set(f"The factorial of {n} is {fact}")

import math
root = tk.Tk()
label = tk.Label(root, text="Enter an integer N and click the button to see its factorial")
label.pack()
entry = tk.Entry(root)
entry.pack()
result = tk.StringVar()
button = tk.Button(root, text="Factorial", command=factorial)
button.pack()
result_label = tk.Label(root, textvariable=result)
result_label.pack()
root.mainloop()