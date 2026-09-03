board = [
    ['','',''],
    ['','',''],
    ['','','']
]
board_values = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
board_map = {
    "1": (0, 0),
    "2": (0, 1),
    "3": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (2, 0),
    "8": (2, 1),
    "9": (2, 2)
}

rev_board_map={
    (0, 0) : "1",
    (0, 1) : "2",
    (0, 2) : "3",
    (1, 0) : "4",
    (1, 1) : "5",
    (1, 2) : "6", 
    (2, 0) : "7",
    (2, 1) : "8",
    (2, 2) : "9"
}

positions_allowed = ["1","2","3","4","5","6","7","8","9"]

def display(board):
    for i in range(len(board)):
        print(board[i])
        print()

def Valid(location):
    if location in positions_allowed:
        return True
    else: 
        return False

GameOver = False

def Check_result(board,symbol,opposition):
    #win
    #row check
    for row in range(3):
        if board[row][0]==board[row][1]==board[row][2]==symbol:
            return 1
    #coloumn check
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i]==symbol:
            return 1
    #diagonal check
    if board[0][0]==board[1][1]==board[2][2]==symbol:
        return 1
    if board[0][2]==board[1][1]==board[2][0]==symbol:
        return 1

    #loss
    #row check
    for row in range(3):
        if board[row][0]==board[row][1]==board[row][2]==opposition:
            return -1
    #coloumn check
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i]==opposition:
            return -1
    #diagonal check
    if board[0][0]==board[1][1]==board[2][2]==opposition:
        return -1
    if board[0][2]==board[1][1]==board[2][0]==opposition:
        return -1
    #tie
    for  row in range(3):
        for col in range(3):
            if board[row][col] == '':
                return None

    else: return 0

def minimax(board,computer_symbol,player_symbol,maximizing):
    result = Check_result(board,computer_symbol,player_symbol)

    #base case
    if result is not None:
        return result

    if maximizing:
        best_score = -float('inf')

        for  row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = computer_symbol
                    score = minimax(board,computer_symbol,player_symbol,False)

                    board[row][col] = ''
                    best_score = max(best_score,score)
        return best_score
    else:
        best_score = float('inf')

        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = player_symbol

                    score = minimax(board,computer_symbol,player_symbol,True)

                    board[row][col] = ''
                    best_score = min(best_score, score)

        return best_score

def best_move(board, computer_symbol, player_symbol):
    best_score = -float('inf')
    best_position = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                board[row][col] = computer_symbol

                score = minimax(board,computer_symbol,player_symbol,False)
                board[row][col] = ''

                if score > best_score:
                    best_score = score
                    best_position = (row, col)

    return best_position

print("1.Play with a Friend\n")
print("2.Play with the computer\n")
choice1 = input()

while choice1 != "1" and choice1 != "2":
    print("Choose from either 1 or 2")
    choice1 = input()

print("1.Choose X\n")
print("2.Choose O\n")
choice2 = input()

while choice2 != "1" and choice2 != "2":
    print("Choose from either X or O")
    choice2 = input()

print("1.Choose First to Play\n")
print("2.Choose Second to Play\n")
choice3 = input()

while choice3 != "1" and choice3 != "2":
    print("Choose from either 1 or 2")
    choice3 = input()

if choice1 == "1":
    if choice2 == "1" and choice3 == "1" or choice2 == "2" and choice3 == "2":
        Player1_symbol = "X"
        Player2_symbol = "O"
    else:
        Player1_symbol = "O"
        Player2_symbol = "X"

if(choice1 == "2"):
    if(choice2 == "1"): 
        Player_symbol = "X"
        Computer_Symbol = "O"
    if(choice2 == "2"): 
        Player_symbol = "O"
        Computer_Symbol = "X"
        
print("This is the values assigned to the box:")
display(board_values)
print("Starting the game.....")
display(board)

Count = 0
Player1_Turn = True
Player2_Turn = False
Result_declared = False

print("Choose location to enter:")

while GameOver is not True and choice1 == "1":

    if Count%2 == 0: 
        Player1_Turn = True
        Player2_Turn = False
    else:
        Player2_Turn = True
        Player1_Turn = False
    location = input()

    if Player1_Turn == True:
        print("Player1:\n")
        
        if Valid(location) == True:
            row,col = board_map[location]
            board[row][col] = Player1_symbol
            positions_allowed.remove(location)
            Count+=1

            print("Board:\n")
            display(board)
        else:
            print("Choose a different position!")

        if Check_result(board,Player1_symbol,Player2_symbol) == 1:
            print("Player1 Won!")
            Result_declared = True
            break

        if not positions_allowed:
            GameOver = True

    if Player2_Turn == True:
        print("Player2:\n")

        if Valid(location) == True:
            row,col = board_map[location]
            board[row][col] = Player2_symbol
            positions_allowed.remove(location)
            Count+=1

            print("Board:\n")
            display(board)
        else:
            print("Choose a different position!")

        if Check_result(board,Player2_symbol,Player1_symbol) == 1:
                print("Player2 Won!")
                Result_declared = True
                break

        if not positions_allowed:
            GameOver = True

while GameOver is not True and choice1 == "2":
    if choice3 == "1":
        Player_move = True
        Comp_move = False
    else:
        Player_move = False
        Comp_move = True

    if Player_move is True:
        print("Player's Move:\n")
        location = input()
                
        if Valid(location) == True:
            row,col = board_map[location]
            board[row][col] = Player_symbol
            positions_allowed.remove(location)
            print("Board:\n")
            display(board)
            choice3 = "2"
        else: 
            print("Choose a different position")

        if Check_result(board,Player_symbol,Computer_Symbol) == 1:
            print("The Player Won!")
            Result_declared = True
            break
    else:
        print("Computer:")
        move = best_move(board, Computer_Symbol, Player_symbol)
        location = rev_board_map[move]
        out_row,out_col = move
        board[out_row][out_col] = Computer_Symbol
        positions_allowed.remove(location)

        print("Board:\n")
        display(board)
        choice3 = "1"
        if Check_result(board,Computer_Symbol,Player_symbol) == 1:
            print("The Computer Won!")
            Result_declared = True
            break
    if not positions_allowed:
        GameOver = True

if GameOver == True and Result_declared == False: print("Tie")