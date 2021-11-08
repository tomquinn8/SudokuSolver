#!/usr/bin/env python3

import sys

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

def isValidMove(puzzle, x, y, guess):
    return guess in getPossibilities(puzzle, x, y)

def getNumbersInRow(puzzle, x):
    return [i for i in puzzle[x] if i > 0]

def getNumbersInColumn(puzzle, y):
    in_column = []
    for i in range(9):
        if puzzle[i][y] > 0:
            in_column.append(puzzle[i][y])
    return in_column

def getNumbersInBox(puzzle, bx, by):
    in_box = []
    for i in range(bx * 3, (bx * 3) + 3):
        for j in range(by * 3, (by * 3) + 3):
            if puzzle[i][j] > 0:
                in_box.append(puzzle[i][j])
    return in_box

def getPossibilities(puzzle, x, y):
    possibilities = [i for i in range(1,10)]
    # Remove possibilities already in row
    in_row = getNumbersInRow(puzzle, x)
    for i in in_row:
        if i in possibilities:
            possibilities.remove(i)
    # Remove possibilities already in column
    in_column = getNumbersInColumn(puzzle, y)
    for i in in_column:
        if i in possibilities:
            possibilities.remove(i)
    # Remove possibilities already in box
    bx = x // 3
    by = y // 3
    in_box = getNumbersInBox(puzzle, bx, by)
    for i in in_box:
        if i in possibilities:
            possibilities.remove(i)
    # Return possibilities
    return possibilities

def eliminateBoxes(puzzle):
    for bx in range(3):
        for by in range(3):
            box_needs = [i for i in range(1,10) if i not in getNumbersInBox(puzzle, bx, by)]
            for i in box_needs:
                possible_squares = []
                for x in range(bx * 3, (bx * 3) + 3):
                    for y in range(by * 3, (by * 3) + 3):
                        if puzzle[x][y] == 0 and isValidMove(puzzle, x, y, i):
                            possible_squares.append((x, y))
                if len(possible_squares) == 1:
                    square = possible_squares[0]
                    puzzle[square[0]][square[1]] = i
                    return True
    return False

def eliminateRows(puzzle):
    for x in range(9):
        row_needs = [i for i in range(1,10) if i not in getNumbersInRow(puzzle, x)]
        for i in row_needs:
            possible_squares = []
            for y in range(9):
                if puzzle[x][y] == 0 and isValidMove(puzzle, x, y, i):
                    possible_squares.append((x,y))
            if len(possible_squares) == 1:
                square = possible_squares[0]
                puzzle[square[0]][square[1]] = i
                return True
    return False

def eliminateColumns(puzzle):
    for y in range(9):
        column_needs = [i for i in range(1,10) if i not in getNumbersInColumn(puzzle, y)]
        for i in column_needs:
            possible_squares = []
            for x in range(9):
                if puzzle[x][y] == 0 and isValidMove(puzzle, x, y, i):
                    possible_squares.append((x,y))
            if len(possible_squares) == 1:
                square = possible_squares[0]
                puzzle[square[0]][square[1]] = i
                return True
    return False

def eliminateSquares(puzzle):
    for x in range(9):
        for y in range(9):
            if puzzle[x][y] == 0:
                possibilities = getPossibilities(puzzle, x, y)
                if len(possibilities) == 1:
                    puzzle[x][y] = possibilities[0]
                    return True
    return False

def isPuzzleSolved(puzzle):
    empty_squares = 0
    for row in puzzle:
        for column in row:
            if column == 0: 
                empty_squares += 1
    # If no empty squares left, puzzle is solved
    return not empty_squares

def tryElimination(puzzle):
    finished = False
    while not finished:
        if eliminateBoxes(puzzle):
            continue
        if eliminateRows(puzzle):
            continue
        if eliminateColumns(puzzle):
            continue
        if eliminateSquares(puzzle):
            continue
        finished = True
    return isPuzzleSolved(puzzle)

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
    solved, unsolved = 0, 0
    for p in puzzles:
        if tryElimination(p):
            solved += 1
            #printPuzzle(p)
        else:
            unsolved +=1
        printPuzzle(p)
        sys.stdout.write(f'\r{solved} Solved. {unsolved} Unsolved.\r')
        sys.stdout.flush()
    print(f'{solved} Solved. {unsolved} Unsolved.')
