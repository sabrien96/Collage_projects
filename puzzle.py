# import numby
import math

# cost_function*
# heurastic*
# loop_track*
# array_of_matrix
# swap func*
# bst search
# count steps
# print
# priv variable

import math
import numpy as np

h = -1
moves = []
goal = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]
puzzle = []  # [[1 ,3, 0],[4,2,5],[7, 8, 6]]


def Cost(matr):
    goal = [['0', '1', '2'],
            ['3', '4', '5'],
            ['6', '7', '8']]
    cost = 0;
    for n in range(0, 2):
        for m in range(0, 2):
            if (goal[n][m] != matr[n][m]):
                cost = +1
    return cost


def loopProb(next, previus):
    for n in range(0, 2):
        for m in range(0, 2):
            if (next != previus):
                return False;
    return True


def swap(puze, row=0, col=0, row1=0, col1=0):
    p = puze
    p[row][col], p[row1][col1] = p[row1][col1], p[row][col]
    return p


def find(adj_matrix, value):
    if value < 0 or value > 8:
        raise Exception("value out of range")
        for r in range(3):
            for c in range(3):
                if adj_matrix[r][c] == value:
                    return [r,c]


def mak_move(puzel):
    if Cost(puzel) == 0:
        return
    else:
        global h
        h = h + 1
        row ,col = find(puzel, 0)
        if row == 2:
            if col == 2:
                puzel_1 = swap(puzel, row, col, row - 1, col)
                puzel_2 = swap(puzel, row, col, row, col - 1)
                if (Cost(puzel_1) <= Cost(puzel_2)):
                    moves[h] = puzel_1
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]):
                            moves[h] = puzel_2

                else:
                    moves[h] = puzel_2
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]):
                            moves[h] = puzel_1
            if col == 1:
                puzel_1 = swap(puzel, row, col, row - 1, col)
                puzel_2 = swap(puzel, row, col, row, col - 1)
                puzel_3 = swap(puzel, row, col, row, col + 1)
                if (Cost(puzel_1) <= Cost(puzel_2) and Cost(puzel_1) <= Cost(puzel_3)):
                    moves[h] = puzel_1
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_2) <= Cost(puzel_3)):
                                moves[h] = puzel_2
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]):
                                        moves[h] = puzel_3
                if (Cost(puzel_2) <= Cost(puzel_1) and Cost(puzel_2) <= Cost(puzel_3)):
                    moves[h] = puzel_2
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_1) <= Cost(puzel_3)):
                                moves[h] = puzel_1
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]):
                                        moves[h] = puzel_3
                if (Cost(puzel_3) <= Cost(puzel_1) and Cost(puzel_3) <= Cost(puzel_2)):
                    moves[h] = puzel_3
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_1) <= Cost(puzel_2)):
                                moves[h] = puzel_1
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]):
                                        moves[h] = puzel_2
            if col == 0:
                puzel_1 = swap(puzel, row, col, row - 1, col)
                puzel_2 = swap(puzel, row, col, row, col + 1)
                if (Cost(puzel_1) <= Cost(puzel_2)):
                    moves[h] = puzel_1
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]):
                            moves[h] = puzel_2
                else:
                    moves[h] = puzel_2
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]):
                            moves[h] = puzel_1

        elif row == 0:
            if col == 0:
                puzel_1 = swap(puzel, row, col, row + 1, col)
                puzel_2 = swap(puzel, row, col, row, col + 1)
                if (Cost(puzel_1) <= Cost(puzel_2)):
                    moves[h] = puzel_1
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]):
                            moves[h] = puzel_2
                else:
                    moves[h] = puzel_2
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]):
                            moves[h] = puzel_1
            if col == 1:
                puzel_1 = swap(puzel, row, col, row + 1, col)
                puzel_2 = swap(puzel, row, col, row, col - 1)
                puzel_3 = swap(puzel, row, col, row, col + 1)
                if (Cost(puzel_1) <= Cost(puzel_2) and Cost(puzel_1) <= Cost(puzel_3)):
                    moves[h] = puzel_1
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_2) <= Cost(puzel_3)):
                                moves[h] = puzel_2
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]):
                                        moves[h] = puzel_3
                if (Cost(puzel_2) <= Cost(puzel_1) and Cost(puzel_2) <= Cost(puzel_3)):
                    moves[h] = puzel_2
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_1) <= Cost(puzel_3)):
                                moves[h] = puzel_1
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]):
                                        moves[h] = puzel_3
                if (Cost(puzel_3) <= Cost(puzel_1) and Cost(puzel_3) <= Cost(puzel_2)):
                    moves[h] = puzel_3
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_1) <= Cost(puzel_2)):
                                moves[h] = puzel_1
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]):
                                        moves[h] = puzel_2
            if col == 2:
                puzel_1 = swap(puzel, row, col, row + 1, col)
                puzel_2 = swap(puzel, row, col, row, col - 1)
                if (Cost(puzel_1) <= Cost(puzel_2)):
                    moves[h] = puzel_1
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]):
                            moves[h] = puzel_2

                else:
                    moves[h] = puzel_2
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]):
                            moves[h] = puzel_2
        elif row == 1:
            if col == 1:
                puzel_1 = swap(puzel, row, col, row + 1, col)
                puzel_4 = swap(puzel, row, col, row - 1, col)
                puzel_2 = swap(puzel, row, col, row, col - 1)
                puzel_3 = swap(puzel, row, col, row, col + 1)
                if (Cost(puzel_4) <= Cost(puzel_2) and Cost(puzel_4) <= Cost(puzel_3) and Cost(puzel_4) <= Cost(
                        puzel_1)):
                    moves[h] = puzel_4
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_1) <= Cost(puzel_2) and Cost(puzel_1) <= Cost(puzel_3)):
                                moves[h] = puzel_1
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                                        if (Cost(puzel_2) <= Cost(puzel_3)):
                                            moves[h] = puzel_2
                                            if h > 1:
                                                if loopProb(moves[h], moves[h - 1]):
                                                    moves[h] = puzel_3
                            if (Cost(puzel_2) <= Cost(puzel_1) and Cost(puzel_2) <= Cost(puzel_3)):
                                moves[h] = puzel_2
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                                        if (Cost(puzel_1) <= Cost(puzel_3)):
                                            moves[h] = puzel_1
                                            if h > 1:
                                                if loopProb(moves[h], moves[h - 1]):
                                                    moves[h] = puzel_3
                            if (Cost(puzel_3) <= Cost(puzel_1) and Cost(puzel_3) <= Cost(puzel_2)):
                                moves[h] = puzel_3
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                                        if (Cost(puzel_1) <= Cost(puzel_2)):
                                            moves[h] = puzel_1
                                            if h > 1:
                                                if loopProb(moves[h], moves[h - 1]):
                                                    moves[h] = puzel_2
                if (Cost(puzel_1) <= Cost(puzel_2) and Cost(puzel_1) <= Cost(puzel_4) and Cost(puzel_1) <= Cost(
                        puzel_3)):
                    moves[h] = puzel_1
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_3) <= Cost(puzel_2) and Cost(puzel_3) <= Cost(puzel_4)):
                                moves[h] = puzel_3
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                                        if (Cost(puzel_2) <= Cost(puzel_4)):
                                            moves[h] = puzel_2
                                            if h > 1:
                                                if loopProb(moves[h], moves[h - 1]):
                                                    moves[h] = puzel_3
                            if (Cost(puzel_2) <= Cost(puzel_3) and Cost(puzel_2) <= Cost(puzel_4)):
                                moves[h] = puzel_2
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                                        if (Cost(puzel_3) <= Cost(puzel_4)):
                                            moves[h] = puzel_3
                                            if h > 1:
                                                if loopProb(moves[h], moves[h - 1]):
                                                    moves[h] = puzel_4
                            if (Cost(puzel_4) <= Cost(puzel_3) and Cost(puzel_4) <= Cost(puzel_2)):
                                moves[h] = puzel_4
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                                        if (Cost(puzel_3) <= Cost(puzel_2)):
                                            moves[h] = puzel_3
                                            if h > 1:
                                                if loopProb(moves[h], moves[h - 1]):
                                                    moves[h] = puzel_2
                if (Cost(puzel_3) <= Cost(puzel_2) and Cost(puzel_3) <= Cost(puzel_4) and Cost(puzel_3) <= Cost(
                        puzel_1)):
                    moves[h] = puzel_3
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_1) <= Cost(puzel_2) and Cost(puzel_1) <= Cost(puzel_4)):
                                moves[h] = puzel_1
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                                        if (Cost(puzel_2) <= Cost(puzel_4)):
                                            moves[h] = puzel_2
                                            if h > 1:
                                                if loopProb(moves[h], moves[h - 1]):
                                                    moves[h] = puzel_4
                            if (Cost(puzel_2) <= Cost(puzel_1) and Cost(puzel_2) <= Cost(puzel_4)):
                                moves[h] = puzel_2
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                                        if (Cost(puzel_1) <= Cost(puzel_4)):
                                            moves[h] = puzel_1
                                            if h > 1:
                                                if loopProb(moves[h], moves[h - 1]):
                                                    moves[h] = puzel_4
                            if (Cost(puzel_4) <= Cost(puzel_1) and Cost(puzel_4) <= Cost(puzel_2)):
                                moves[h] = puzel_4
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                                        if (Cost(puzel_1) <= Cost(puzel_2)):
                                            moves[h] = puzel_1
                                            if h > 1:
                                                if loopProb(moves[h], moves[h - 1]):
                                                    moves[h] = puzel_2
                if (Cost(puzel_2) <= Cost(puzel_3) and Cost(puzel_2) <= Cost(puzel_4) and Cost(puzel_2) <= Cost(
                        puzel_1)):
                    moves[h] = puzel_2
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_1) <= Cost(puzel_3) and Cost(puzel_1) <= Cost(puzel_4)):
                                moves[h] = puzel_1
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                                        if (Cost(puzel_3) <= Cost(puzel_4)):
                                            moves[h] = puzel_3
                                            if h > 1:
                                                if loopProb(moves[h], moves[h - 1]):
                                                    moves[h] = puzel_4
                            if (Cost(puzel_3) <= Cost(puzel_1) and Cost(puzel_3) <= Cost(puzel_4)):
                                moves[h] = puzel_3
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                                        if (Cost(puzel_1) <= Cost(puzel_4)):
                                            moves[h] = puzel_1
                                            if h > 1:
                                                if loopProb(moves[h], moves[h - 1]):
                                                    moves[h] = puzel_4
                            if (Cost(puzel_4) <= Cost(puzel_1) and Cost(puzel_4) <= Cost(puzel_3)):
                                moves[h] = puzel_4
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                                        if (Cost(puzel_1) <= Cost(puzel_3)):
                                            moves[h] = puzel_1
                                            if h > 1:
                                                if loopProb(moves[h], moves[h - 1]):
                                                    moves[h] = puzel_3
            if col == 0:
                puzel_1 = swap(puzel, row, col, row + 1, col)
                puzel_2 = swap(puzel, row, col, row - 1, col)
                puzel_3 = swap(puzel, row, col, row, col + 1)
                if (Cost(puzel_1) <= Cost(puzel_2) and Cost(puzel_1) <= Cost(puzel_3)):
                    moves[h] = puzel_1
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_2) <= Cost(puzel_3)):
                                moves[h] = puzel_2
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]):
                                        moves[h] = puzel_3
                if (Cost(puzel_2) <= Cost(puzel_1) and Cost(puzel_2) <= Cost(puzel_3)):
                    moves[h] = puzel_2
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_1) <= Cost(puzel_3)):
                                moves[h] = puzel_1
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]):
                                        moves[h] = puzel_3
                if (Cost(puzel_3) <= Cost(puzel_1) and Cost(puzel_3) <= Cost(puzel_2)):
                    moves[h] = puzel_3
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_1) <= Cost(puzel_2)):
                                moves[h] = puzel_1
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]):
                                        moves[h] = puzel_2
            if col == 1:
                puzel_1 = swap(puzel, row, col, row + 1, col)
                puzel_2 = swap(puzel, row, col, row, col - 1)
                puzel_3 = swap(puzel, row, col, row - 1, col)
                if (Cost(puzel_1) <= Cost(puzel_2) and Cost(puzel_1) <= Cost(puzel_3)):
                    moves[h] = puzel_1
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_2) <= Cost(puzel_3)):
                                moves[h] = puzel_2
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]):
                                        moves[h] = puzel_3
                if (Cost(puzel_2) <= Cost(puzel_1) and Cost(puzel_2) <= Cost(puzel_3)):
                    moves[h] = puzel_2
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_1) <= Cost(puzel_3)):
                                moves[h] = puzel_1
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]):
                                        moves[h] = puzel_3
                if (Cost(puzel_3) <= Cost(puzel_1) and Cost(puzel_3) <= Cost(puzel_2)):
                    moves[h] = puzel_3
                    if h > 1:
                        if loopProb(moves[h], moves[h - 1]) or loopProb(moves[h], moves[h - 2]):
                            if (Cost(puzel_1) <= Cost(puzel_2)):
                                moves[h] = puzel_1
                                if h > 1:
                                    if loopProb(moves[h], moves[h - 1]):
                                        moves[h] = puzel_2

            return mak_move(moves[h])


def print_puzzle(p):
    str = ''
    for i in range(3):
        for j in range(3):
            if p[i][j] == '0':
                str += '  '
            else:
                str += p[i][j] + ' '
        str += '\n'
    print(str)


def main():
    # try:
    with open('puzzle', 'r') as f:
        for line in f:
            puzzle.append(line.strip().split(' '))
        mak_move(puzzle)
        for stat in moves:
            print_puzzle(stat)
        global h
        print("Minimum number of moves =", h)


# except:
#  print("sorry gehad u just waste your time ")

if __name__ == "__main__":
    main()

# def tree(puzzle):






