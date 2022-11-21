bill = []
price = []
def showbill() :
    total = 0
    for i in range(len(bill)) :
        total = total + price[i]
        print(bill[i], price[i] , "Baht")
    print("Total :",total)
while True :
    databill = input("Eat : ").capitalize()
    if databill != "End" :
        bill.append(databill)
    elif databill == "End" :
        showbill()
        break
    dataprice = int(input("Price : "))
    price.append(dataprice)




