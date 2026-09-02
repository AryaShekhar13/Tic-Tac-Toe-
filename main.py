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
choice = input()

while choice != "1" and choice != "2":
    print("Choose from either 1 or 2")
    choice = input()

print("This is the values assigned to the box:")
display(board_values)
print("Starting the game.....")
display(board)


while GameOver != True:
    print("Choose location to enter:")
    location = input()
    if Valid(location) == True:
        row,col = board_map[location]
        board[row][col]
        positions_allowed.remove(location)
    else:
        print("Choose a different position!") 

    if not positions_allowed:
        GameOver = True