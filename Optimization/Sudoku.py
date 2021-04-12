#!/usr/bin/python3

"""
    @author -> Arturo Negreiros
    @description -> Sudoku automation solver
"""

sudoku_board = [
    [3, 0, 5, 6, 2, 9, 0, 0, 7],
    [7, 0, 6, 1, 0, 8, 0, 0, 0],
    [8, 0, 1, 0, 0, 0, 2, 6, 5],
    [0, 0, 3, 0, 0, 5, 0, 7, 0],
    [6, 8, 7, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 7, 0, 0, 6, 0, 0],
    [4, 7, 9, 5, 8, 0, 0, 2, 0],
    [1, 0, 0, 4, 3, 0, 5, 0, 9],
    [0, 0, 8, 9, 0, 0, 0, 0, 6]
]


def print_board(board):
    #print("SUDOKU")
    print("\n")
    base = "_" * 34
    position = 1
    base_position = 1
    print(base, "\n")
    for x in board:
        print("| ", end="")
        for y in x:
            if y == 0:
                print("   ", end="")
            else:
                print(y," ", end="")
            if position != 0 and  position % 3  == 0:
                print("| ", end="")
            position += 1
        print("")

        if base_position %3 == 0 and base_position != 0:
            print(base, "\n")
        base_position += 1



def solve_sudoku(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for x in range(1,10):
        if check_valid_number(x, board, (row, col)):
            board[row][col] = x

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def find_empty(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 0:
                return (x, y)

    return None

def check_valid_number(number, board, pos):

    # first set the initial positions to insert the number
    # checking if the numbers is present in the column, row
    # and square
    # this test is for the first portion square

    # checking the rows
    # 'pos' parameter is a tuple withe the positions with zero value
    for x in range(len(board[0])):
        if board[pos[0]][x] == number and pos[1] != x:
            return False

    # checking columns
    for y in range(len(board)):
        if board[y][pos[1]]  == number and pos[0]  != y:
            return False

    # checking the box
    board_x = pos[1] // 3
    board_y = pos[0] // 3

    for i in range(board_y *3, board_y*3 + 3):
        for j in range(board_x*3, board_x*3 + 3):
            if board[i][j] == number and (i,j) != pos:
                return  False

    return True
#def main():
print_board(sudoku_board)
print("[*] solving")
solve_sudoku(sudoku_board)
print_board(sudoku_board)




"""
if __name__ == '__main__':
    main()
"""