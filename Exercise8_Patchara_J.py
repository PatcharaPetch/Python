usernameinput = input("Username : ",)
passwordinput = input("Password : ",)
if usernameinput=="nongpetch" and passwordinput=="1234" :
    print("----------------------------------------------------")
    print("--------------Welcome To Petch'Shop-----------------")
    print("----------------------------------------------------")
    print("Banana x1    =  20 THB")
    print("Apple x1     =  15 THB")
    print("Pencil x1    =  10 THB")
    print("eraser x1    =  5  THB")
    print("----------------------------------------------------")
    thing = input("คุณต้องการอะไร : ",)
    num = int(input("จำนวนเท่าไหร่ : ",))
    if thing=="Banana" :
        pricebanana = 20*num
        print("ราคารวม : ",pricebanana)
    elif thing=="Apple" :
        priceapple = 15*num
        print("ราคารวม : ",priceapple)
    elif thing=="Pencil" :
        pricepencil = 10*num
        print("ราคารวม : ",pricepencil)
    elif thing=="eraser" :
        priceeraser = 5*num
        print("ราคารวม : ",priceeraser)
    else :
        print("ขออภัยเราไม่มีสินค้าที่ท่านระบุ")
else :
    print("ไม่พบผู้ใช้งานในระบบ")
