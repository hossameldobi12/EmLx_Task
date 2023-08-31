import tkinter as tk

def red():
    canvas.itemconfig(circle, fill="red")

def white():
    canvas.itemconfig(circle, fill="white")


root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
circle = canvas.create_oval(100, 100, 200, 200, fill="white")
button_red = tk.Button(root, text="Red", command=red)
button_white = tk.Button(root, text="White", command=white)
canvas.pack()
button_red.pack(side=tk.LEFT)
button_white.pack(side=tk.RIGHT)
root.mainloop()