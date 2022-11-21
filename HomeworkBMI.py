from tkinter import *
def calBMI(event) :
    BMI = float(textBoxWeight.get())/(float(textBoxHeight.get())**2)
    if BMI >= 30 :
        labelResult.configure(text="อ้วนมาก")
    elif BMI >= 25 and BMI <= 29.9 :
        labelResult.configure(text="อ้วน")
    elif BMI >= 23 and BMI <= 24.9 :
        labelResult.configure(text="น้ำหนักเกิน")
    elif BMI >= 18.6 and BMI <= 22.9 :
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    elif BMI <= 18.5 :
        labelResult.configure(text="ผอมเกินไป")

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