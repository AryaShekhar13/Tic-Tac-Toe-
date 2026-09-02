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

if choice1 == "1":
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
    if(choice2 == "1"): Player_symbol = "X"
    if(choice2 == "2"): Player_symbol = "O"
        
print("This is the values assigned to the box:")
display(board_values)
print("Starting the game.....")
display(board)

Count = 0
Player1_Turn = True
Player2_Turn = False
Comp = False
if choice1 == "2": Comp = False

print("Choose location to enter:")

while GameOver != True:
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

        if not positions_allowed:
            GameOver = True

    if Player2_Turn == True:
        print("Player1:\n")
        if Valid(location) == True:
            row,col = board_map[location]
            board[row][col] = Player2_symbol
            positions_allowed.remove(location)
            Count+=1

            print("Board:\n")
            display(board)
        else:
            print("Choose a different position!")

        if not positions_allowed:
            GameOver = True