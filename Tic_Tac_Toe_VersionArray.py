from glob import glob


theboard = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
turn = 2 ## 2 = O , 1 = x
game_over = False


def printBoard():
    for a in range(3):
        for b in range(3):
            print(
                "|" + ("X" if theboard[a][b] == 1 else "O" if theboard[a][b] == 2 else "-"), end=" ")
        print("|")

def switch_turn():
    global turn
    if turn == 2:
        turn = 1
    else:
        if turn == 1 :
            turn = 2

def gameXO():
    printBoard()
    while game_over == False:
        user = int(input("Enter : ")) - 1
        x = user%3
        y = 2 - user//3
        theboard[y][x] = turn
        printBoard()
        checkwin()
        switch_turn()
        if game_over == True:
            if turn == 1:
                print(" X is Win ")
                break
            elif turn == 2 :
                print(" O is Win ")
                break
    

def checkwin():
    global game_over
    for i in range(3): 
        if theboard[i][0] == theboard[i][1] == theboard[i][2] != 0 :
            game_over = True
        if theboard[0][i] == theboard[1][i] == theboard[2][i] != 0 :
            game_over = True
    if theboard[0][0] == theboard[1][1] == theboard[2][2] != 0:
        game_over = True
    if theboard[0][2] == theboard[1][1] == theboard[2][0] != 0 :
        game_over = True

gameXO()