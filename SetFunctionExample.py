userinput = int(input("Enter Number of your fav fruits : "))
myfruits = set() #ถ้าใช้ {} จะกลายเป็น dictionary
while len(myfruits) < userinput :
    myfruits.add(input("Fruit : "))
