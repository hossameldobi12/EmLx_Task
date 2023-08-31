'''
info : this file to sum or sub two numbers
Name : Hossam Adel Mostafa

'''


import tkinter as tk

def sum():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    sum = num1 + num2
    result.set(f"The sum of {num1} and {num2} is {sum}")

def sub():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    sub = num1 - num2
    result.set(f"The sub of {num1} and {num2} is {sub}")
    
    
root = tk.Tk()
label = tk.Label(root, text="Enter two integers and choose an operation")
label.pack()
entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()
result = tk.StringVar()
button1 = tk.Button(root, text="Sum", command=sum)
button1.pack()
button2 = tk.Button(root, text="Sub", command=sub)
button2.pack()
result_label = tk.Label(root, textvariable=result)
result_label.pack()
root.mainloop()