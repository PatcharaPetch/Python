menu = {"ข้าวมันไก่":50,"ข้าวหมูทอด":60,"ข้าวแมวทอด":80,"ข้าวปลาทอด":100}
bill = []
def showbill() :
    total = 0
    for i in range(len(bill)) :
        total = total + bill[i][1]
        print(bill[i][0], bill[i][1] , "Baht")
    print("Total :",total)
while True :
    databill = input("Eat : ")
    if databill != "End" :
        bill.append([databill,menu[databill]])
    elif databill == "End" :
        showbill()
        break
