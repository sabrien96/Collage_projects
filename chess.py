import copy
import itertools
import random
board = [8]
for i in range(8):
    board[i]=new [8]

size = 8
board[random.randint(0,7)][random.randint(0,7)]="X"
def print_paten(board):
    for i in range(8):
        for j in range(8):
            print(board[i][j])


def is_safe(board, row, col, size):
    """Check if it's safe to place a queen at board[x][y]"""

    # check row on left side
    for iy in range(8):
        if board[row][iy] == "X":
            return False

    ix, iy = row, col
    while ix >= 0 and iy >= 0:
        if board[ix][iy] == "X":
            return False
        ix -= 1
        iy -= 1

    jx, jy = row, col
    while jx < size and jy >= 0:
        if board[jx][jy] == "X":
            return False
        jx += 1
        jy -= 1

    return True

def solve(board, col, size):
    """Use backtracking to find all solutions"""
    # base case
    if col >= size:
        return

    for i in range(size):
        if is_safe(board, i, col, size):
            board[i][col] = "X"
            print_paten(board)
            if col == size - 1:
                board[i][col] = 0
                return
            solve(board, col + 1, size)
            # backtrack
            board[i][col] = 0

solve(board, 0, 8)


