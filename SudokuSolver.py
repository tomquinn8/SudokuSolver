#!/usr/bin/env python3

from time import sleep
from os import system

def printPuzzle(puzzle):
    print(chr(9484) + ' ' + '- ' * 11 + chr(9488))
    for index,row in enumerate(puzzle):
        print('| ', end='')
        print(' '.join([str(i) if i > 0 else ' ' for i in row[0:3]]), end='')
        print(' | ', end='')
        print(' '.join([str(i) if i > 0 else ' ' for i in row[3:6]]), end='')
        print(' | ', end='')
        print(' '.join([str(i) if i > 0 else ' ' for i in row[6:9]]), end='')
        print(' |')
        if index % 3 == 2 and index + 1 < len(puzzle):
            print('| ' + '- ' * 11 + '|')
    print(chr(9492) + ' ' + '- ' * 11 + chr(9496))

def getPossibilities(puzzle, x, y):
    possibilities = [i for i in range(1,10)]
    # Remove possibilities already in row
    in_row = [i for i in puzzle[x] if i > 0]
    for i in in_row:
        if i in possibilities:
            possibilities.remove(i)
    # Remove possibilities already in column
    in_column = []
    for i in range(9):
        if puzzle[i][y] > 0:
            in_column.append(puzzle[i][y])
    for i in in_column:
        if i in possibilities:
            possibilities.remove(i)
    # Remove possibilities already in box
    in_box = []
    bx = x // 3
    by = y // 3
    for i in range(bx * 3, (bx * 3) + 3):
        for j in range(by * 3, (by * 3) + 3):
            if puzzle[i][j] > 0:
                in_box.append(puzzle[i][j])
    for i in in_box:
        if i in possibilities:
            possibilities.remove(i)
    # Return possibilities
    return possibilities

def trySubstitution(puzzle):
    finished = False
    x, y = 0, 0
    while not finished:
        if puzzle[x][y] == 0:
            possibilities = getPossibilities(puzzle, x, y)
            if len(possibilities) == 1:
                puzzle[x][y] = possibilities[0]
                x, y = 0, 0
        if x == 8 and y == 8: 
            finished = True
        elif x < 8:
            x += 1
        else:
            y += 1
            x = 0
    printPuzzle(puzzle)
    empty_squares = 0
    for row in puzzle:
        for column in row:
            if column ==0: 
                empty_squares +=1
    if empty_squares == 0:
        return True
    else:
        return False

def loadPuzzles(file):
    puzzles = []
    with open(file, 'r') as f:
        for line in f:
            line = [0 if c == '.' else int(c) for c in line.rstrip()]
            puzzle = [
                line[0:9],line[9:18],line[18:27],
                line[27:36],line[36:45],line[45:54],
                line[54:63],line[63:72],line[72:81]
                ]
            puzzles.append(puzzle)
    return puzzles


if __name__=='__main__':
    puzzles = loadPuzzles('puzzles.txt')
    solved, unsolved = 0,0
    for p in puzzles:
        if trySubstitution(p):
            solved += 1
        else:
            unsolved +=1
        print(f'{solved} Solved. {unsolved} Unsolved.')
