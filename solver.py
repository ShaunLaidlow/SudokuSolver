board = [
    [0,0,0,9,8,0,6,1,0],
    [4,0,0,0,6,0,0,0,0],
    [0,0,9,5,0,0,0,2,7],
    [0,0,0,2,0,0,7,0,0],
    [5,4,0,0,0,0,0,8,6],
    [0,7,6,0,5,0,0,0,0],
    [0,6,1,0,9,5,8,3,2],
    [2,9,4,0,3,7,5,6,0],
    [8,0,0,0,2,1,0,0,0]
]

#Prints stylized sudoku grid
def print_sudoku(board):
    for i in range(len(board)):
        # Loop through every row. Break up every 3 rows with dashes to form grid
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        # Loop through every col. Break up every 3 cols with | to form grid
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            #if at the end of the row, print final digit and start new row
            if j == 8:
                print(board[i][j])
            #else print board without newline
            else:
                print(str(board[i][j])+ " ", end="")

#Finds zeros in the game board and returns it's grid location (row,col)
def find_zero(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) #row, col
    return None

#Validate Number Doesn't Conflict with Current Grid
def validate_number(board,test_num,test_position):
    #Check if number exists in the row
    for j in range(len(board[0])):
        if test_num == board[test_position[0]][j] and test_position[1] != j:
            return False

    #Check if number exists in the col
    for i in range(len(board)):
        if test_num == board[i][test_position[1]] and test_position[0] != i:
            return False

    #Check if number exists in the grid square
    x_box = test_position[1] // 3
    y_box = test_position[0] // 3
    
    for j in range(x_box * 3, x_box * 3 + 3):
        for i in range(y_box * 3, y_box * 3 + 3):
            if board[i][j] == test_num and test_position[0] != i and test_position[1] != j:
                return False
                
    #Return True if all conditions are satisfied            
    return True

    





print_sudoku(board)