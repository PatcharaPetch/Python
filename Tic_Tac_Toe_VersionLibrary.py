theboard = {"7": " " , "8": " " , "9": " " ,
            "4": " " , "5": " " , "6": " " ,
            "1": " " , "2": " " , "3": " " }
            
def printBoard(board):
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["1"] + "|" + board["2"] + "|" + board["3"])

def gameXO():
    turn = 'X'
    count = 0
    i = 0
    while i < 10 :
        printBoard(theboard)
        print("It's your turn," + turn )
        move = input()       
        if theboard[move] == " " :
            theboard[move] = turn
            count = count + 1
        else:
            print("That place is already filled")
            continue
        i = i + 1
        if count >= 5:
            if theboard["7"] == theboard["8"] == theboard["9"] != " " : # across the top
                printBoard(theboard)
                print("\nGame Over\n")                
                print(" **** " + turn + " won ****")                
                break
            elif theboard["4"] == theboard["5"] == theboard["6"] != " " : # across the middle
                printBoard(theboard)
                print("\nGame Over\n")                
                print(" **** " + turn + " won ****")
                break
            elif theboard["1"] == theboard["2"] == theboard["3"] != ' ' : # across the bottom
                printBoard(theboard)
                print("\nGame Over\n")                
                print(" **** " + turn + " won ****")
                break
            elif theboard["1"] == theboard["4"] == theboard["7"] != ' ' : # down the left side
                printBoard(theboard)
                print("\nGame Over\n")                
                print(" **** " + turn + " won ****")
                break
            elif theboard["2"] == theboard["5"] == theboard["8"] != ' ' : # down the middle
                printBoard(theboard)
                print("\nGame Over\n")                
                print(" **** " +turn + " won ****")
                break
            elif theboard["3"] == theboard["6"] == theboard["9"] != ' ' : # down the right side
                printBoard(theboard)
                print("\nGame Over\n")                
                print(" **** " +turn + " won ****")
                break 
            elif theboard["7"] == theboard["5"] == theboard['3'] != ' ' : # diagonal
                printBoard(theboard)
                print("\nGame Over\n")                
                print(" **** " +turn + " won ****")
                break
            elif theboard['1'] == theboard['5'] == theboard['9'] != ' ' : # diagonal
                printBoard(theboard)
                print("\nGame Over\n")                
                print(" **** " +turn + " won ****")
                break 
        if count == 9:
            print("\nGame Over\n")                
            print("It's a Tie !!")
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'     
gameXO()
