def caldivide() :
    a = int(input("Num1 : "))
    b = int(input("Num2 : "))
    print(a / b)
try :
    caldivide()
except ValueError :
    print("Value Error ! Please Re-Enter Number Again")
    caldivide()
except ZeroDivisionError :
    print("You can't Enter 0")
    caldivide()
