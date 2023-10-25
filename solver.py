board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
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





print_sudoku(board)