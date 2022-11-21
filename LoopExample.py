user = int(input("Put Number : "))
for i in range(user) :
    print(" "*(user-i)+"*"*((2*i)+1))
for j in range(user) :
    print(" "*(j+2)+"*"*(2*(user-j)))
