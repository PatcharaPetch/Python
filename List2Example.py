bill = []
def showbill() :
    total = 0
    for i in range(len(bill)) :
        total = total + bill[i][1]
        print(bill[i][0], bill[i][1] , "Baht")
    print("Total :",total)
while True :
    databill = input("Eat : ").capitalize()
    if databill != "End" :
        dataprice = int(input("Price : "))
        bill.append([databill,dataprice])
    elif databill == "End" :
        showbill()
        break




