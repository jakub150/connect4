empty = 'O'
red_token = 'R'
yellow_token = 'Y'

PLAYER_1 = 0
PLAYER_2 = 1
player = PLAYER_1

grid = []
width = 0
height = 0
win_length = 0

def Create_Grid():
    global width
    global height
    global grid

    for i in range(width):
        temp = []
        for j in range(height):
            temp.append(empty)
        grid.append(temp)

def Print_Grid():
    global width
    global height
    global grid

    print("Game grid status:\n")
    for i in range(height):
        print("|", end="")
        for j in range(width):
            print(f"{grid[j][height-1-i]}|", end="")
        print("")
    
    for i in range(width):
        print(f" {i}", end="")
    print("")

def Initiate_Game_Grid():
    print("Initiating game grid...\n")
    global width
    width = int(input("Please enter the width of grid (greater than 0) :"))
    if width <= 0:
        raise Exception("Sorry, no numbers below or equal zero")
    global height
    height = int(input("Please enter the height of grid (greater than 0) :"))
    if height <= 0:
        raise Exception("Sorry, no numbers below or equal zero")
    global win_length
    win_length = int(input("Please enter the winning row length (greater than 2) :"))
    if win_length <= 0:
        raise Exception("Sorry, no numbers below or equal two")

    Create_Grid()
    print("Done!\n")

    Print_Grid()

    print("For player 1, you will use ther red token. Symbol:R")
    print("For player 2, you will use ther yellow token. Symbol:Y")

def Player_Turn():
    print(f"=============PLAYER {player+1}'s Turn=============")
    #print("Current grid state:")
    Print_Grid()

    column = int(input("Please pick a column:"))
    if (column < 0 or column >= width):
        raise Exception("Sorry, invalid input")
    print("")

    for i in range(height):
        if(grid[column][i] == empty):
            grid[column][i] = red_token if player==PLAYER_1 else yellow_token
            break
        if(i == height-1):
            raise Exception("Sorry, this column is full.")

def equal_symbols(check_list):
    for i in range(win_length):
        if(i == win_length-1):
            return True
        if(check_list[i] == empty):
            return False
        if(check_list[i] != check_list[i+1]):
            return False

def Check_Victory_Row():
    for i in range(width - win_length + 1):
        for j in range(height):
            temp = []
            for k in range(win_length):
                #print(f"i={i}, j={j}, k={k}")
                temp.append(grid[i+k][j])
            if(equal_symbols(temp)):
                return True
    return False

def Check_Victory_Column():
    for i in range(width):
        for j in range(height - win_length + 1):
            temp = []
            for k in range(win_length):
                #print(f"i={i}, j={j}, k={k}")
                temp.append(grid[i][j+k])
            if(equal_symbols(temp)):
                return True
    return False

def Check_Victory_Left_Diagonal():
    for i in range(width - win_length + 1):
        for j in range(height - win_length + 1):
            temp = []
            for k in range(win_length):
                #print(f"i={i}, j={j}, k={k}")
                temp.append(grid[i+k][j+k])
            if(equal_symbols(temp)):
                return True
    return False

def Check_Victory_Right_Diagonal():
    for i in range(width - win_length + 1):
        for j in range(height - win_length + 1):
            temp = []
            for k in range(win_length):
                #print(f"i={i}, j={j}, k={k}")
                temp.append(grid[i+k][j+win_length-1-k])
            if(equal_symbols(temp)):
                return True
    return False

def Check_Victory():
    return Check_Victory_Row() or Check_Victory_Column() or Check_Victory_Left_Diagonal() or Check_Victory_Right_Diagonal()

def Check_Draw():
    for i in range(width):
        for j in range(height):
            if(grid[i][j] == empty):
                return False
    return True

def Change_Player_Turn():
    global player
    player = PLAYER_1 if player == PLAYER_2 else PLAYER_2

Initiate_Game_Grid()

while 1:
    Player_Turn()
    if(Check_Victory()):
        print(f"GAME ENDS. PLAYER {player+1} WON THE GAME!")
        break
    if(Check_Draw()):
        print("GAME ENDS. IT'S A DRAW!")
        break
    Change_Player_Turn()

#print(f"Check_Victory_Row: {Check_Victory_Row()}")
#print(f"Check_Victory_Column: {Check_Victory_Column()}")
#print(f"Check_Victory_Left_Diagonal: {Check_Victory_Left_Diagonal()}")
#print(f"Check_Victory_Right_Diagonal: {Check_Victory_Right_Diagonal()}")

Print_Grid()