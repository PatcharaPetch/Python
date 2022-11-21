from tkinter import *
def sayHelloWorld() :
    print("Hello World")
    print("Patchara Jianjinda")
mainwindow = Tk()
button = Button(mainwindow,text = "Click Me 1",command = sayHelloWorld).grid(row=0,column=0)
button2 = Button(mainwindow,text = "Click Me 2",command = sayHelloWorld).grid(row=0,column=1)
button3 = Button(mainwindow,text = "Click Me 3",command = sayHelloWorld).grid(row=1,column=0)

mainwindow.mainloop()
