Round = int(input("Please Enter Number : "))
sum = 0
for x in range(Round) :
    number = int(input("x"+str(x+1)+ ": "))
    sum = sum + number
print(sum)