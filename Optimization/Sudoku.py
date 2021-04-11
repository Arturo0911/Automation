#!/usr/bin/python3

import random

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

    if board is None:
        print("No solutions!")
        return

    num_rows = len(board)
    num_cols = len(board[0])
    for r in range(num_rows):
        for c in range(num_cols):
            if board[r][c] == 0:
                number = random.randint(1,9)
                if check_valid_number(number, board):
                    board[r][c] = number

    return board

def re_solve(board):
    for x in range(9):
        for y in range(9):
            random_number = random.randint(1,9)
            if check_valid_number(random_number, board):
                board[x][y] = random_number
    return board




def main():
    print_board(sudoku_board)
    sudoku_solved = solve_sudoku(sudoku_board)
    while True:
        
        print_board(sudoku_solved)
        if not_repeat_in_square(sudoku_solved, 0, 0):
            break
        else:
            re_solve(sudoku_solved)

def not_repeat_in_square(board,positions_y,positions_x):

    # An stack to add any number in a portion of square
    # from the sudoku board
    stack = list()
    for x in board:
        for y in x:
            #print(y, end= "")
            if y not in stack:
                stack.append(y)
            else:
                pass
            if positions_x ==2 and positions_x != 0:
                break
            positions_x += 1
        if positions_y  == 3:
            break
        #print("\n")
        positions_y += 1

    # only if the size of the stack representing
    # the values of the portions square from sudoku
    # board, is equal to 9 then one square is right
    return len(stack) == 9


def find_empty(board):
    
    for x in range(len(board)):
        for y in range(len(board[0])):
            
            if board[x][y] == 0:
                return (x,y)

    return None


# number to be validated
# game board
# tuple with the positions with zeros

def check_valid_number(number, board, pos):

    # first set the initial positions to insert the number
    # checking if the numbers is present in the column, row
    # and square
    # this test is for the first portion square

    is_valid_row = True
    row_position = 0
    # Here the validation is for the row
    for x in board:

        if number not in x:
            is_valid_row = True
        else:
            is_valid_row = False
        
        if row_position == 3:
            break
        row_position += 1

    for x in board:

        for y in range(3):

            if x[y] != number:
                is_valid_row = True
            else:
                is_valid_row = False

    return is_valid_row




if __name__ == '__main__':
    main()
