'''
info : this task for controlling buttons using tkinter
Name : Hossam Adel Mostafa

'''

import tkinter

def button_one():
    print("button one pressd")
def button_two():
    print("button two pressd")
def button_three():
    print("button three pressd")
def button_four():
    print("button four pressd")


window = tkinter.Tk()
window.title("buttons")
window.geometry("500x500+700+300")
window.resizable(False,False)
ButtonOne = tkinter.Button(window,text="ButtonOne",width=10,command=button_one)
ButtonOne.place(x=195,y=0)
ButtonTwo = tkinter.Button(window,text="ButtonTwo",width=10,command=button_two)
ButtonTwo.place(x=87,y=22)
ButtonThree = tkinter.Button(window,text="ButtonThree",width=10,command=button_three)
ButtonThree.place(x=300,y=27)
ButtonFour = tkinter.Button(window,text="ButtonFour",width=10,command=button_four)
ButtonFour.place(x=195,y=50)
window.mainloop()
