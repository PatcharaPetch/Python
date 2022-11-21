def login() :
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showmenu()
def showmenu() :
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    if menuselect() == 1 :
        print(calprice())
def menuselect() :
    userSelected = int(input(">> "))
    return userSelected
def calvat(price) :
    vat = 7
    result = price + (price * vat / 100)
    return result
def calprice() :
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return calvat(price1 + price2)
login()