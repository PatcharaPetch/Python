from tkinter import *
def calBMI(event) :
    labelResult.configure(text = float(textBoxWeight.get())/(float(textBoxHeight.get())**2))

main = Tk()
labelHeight = Label(main,text="ส่วนสูง (เมตร)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(main)
textBoxHeight.grid(row=0,column=1)


labelWeight = Label(main,text="น้ำหนัก (กิโลกรัม)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(main)
textBoxWeight.grid(row=1,column=1)


calButton = Button(main,text="คำนวณ")
calButton.bind("<Button-1>",calBMI)
calButton.grid(row=2,column=0)

labelResult = Label(main,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
main.mainloop()