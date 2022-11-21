from tkinter import *
def LeftClickButton(event) :
    print("Left Click!!")
def RightClickButton(event) :
    print("Right Click!!")
def DoubleClick(event) :
    print("Double Click!!")

main = Tk()
button = Button(main,text="My Button !!")
button.pack()
button.bind("<Button-1>",LeftClickButton)
button.bind("<Button-3>",RightClickButton)
button.bind("<Double-1>",DoubleClick)
main.mainloop()
