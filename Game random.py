import random
money = 50
b = "Yes"
a = random.randint(1,2)
print("Welcome to my game")
print("Let's Play game")
while money > 0 :
    while b.capitalize() == "Yes" and money > 0 :
        userinput = int(input("Head[1] or Tail[2] : "))
        if userinput == a :
            money = money + 10
            print("You got 10 Baht")
            print("Now You have ",money," baht")
            b = input("You want to play again (Yes or No) : ")
            if b.capitalize() == "No" :
                print("You Choose Exit this game")
                print("Thank For playing")
                break
            a = random.randint(1,2)
        elif userinput != a :
            money = money - 20
            print("You lost 20 baht")
            print("Now You have ",money," baht")
            b = input("You want to play again (Yes or No) : ")
            if b.capitalize() == "No" :
                print("You Choose Exit this game")
                print("Thank For playing")
                break
            a = random.randint(1,2)
        else :
            print("Please Try again")
print("You can't play this game , you don't have money")
    


