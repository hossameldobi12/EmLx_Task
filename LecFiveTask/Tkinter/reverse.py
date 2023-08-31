'''
info : this file for reserve function using tkinter
name : Hosssam Adel Mostafa

'''
import tkinter
def reverse():
    str = enter.get()
    str1 = str[::-1]
    label_reverse = tkinter.Label(window,text= f"{str1}")
    label_reverse.pack()
    

window = tkinter.Tk()
window.title("buttons")
window.geometry("500x500+700+300")
window.resizable(False,False)
label =tkinter.Label(window,text = "entre word")
enter = tkinter.Entry(window)
button = tkinter.Button(window,text="validate",width=10,command=reverse)
label.pack()
enter.pack()
button.pack()
window.mainloop()




