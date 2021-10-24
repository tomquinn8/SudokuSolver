#!/usr/bin/env python3

puzzle = [
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

possibilities = []

def print_puzzle(puzzle):
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

def print_current_status(puzzle):
    total_squares = sum([len(row) for row in puzzle])
    solved = 0
    unsolved = 0
    for row in puzzle:
        for column in row:
            if column > 0:
                solved += 1
            else:
                unsolved += 1
    print(f'{total_squares} squares')
    print(f'{solved} solved')
    print(f'{unsolved} to be solved')

def update_possibilities(puzzle):
    # Destroy and recreate the 'possibilities' list
    global possibilities
    possibilities = []
    for x in range(9):
        possibilities.append([])
        for y in range(9):
            possibilities[x].append([])
            if puzzle[x][y] > 0:
                possibilities[x][y] = [puzzle[x][y]]
            else:
                possibilities[x][y] = [i + 1 for i in range(9)]

    # Update possibilities based on rows
    for x, row in enumerate(puzzle):
        found = [i for i in row if i > 0]
        for y in range(9):
            for i in found:
                if i in possibilities[x][y]:
                    possibilities[x][y].remove(i)

    # Update possibilties based on columns
    for y in range(9):
        found = []
        for x in range(9):
             if puzzle[x][y] > 0:
                found.append(puzzle[x][y])
        for x in range(9):
            for i in found:
                if i in possibilities[x][y]:
                    possibilities[x][y].remove(i)

    # Update possibilities based on boxes
    # TODO

def update_puzzle():
    global puzzle
    global possibilities
    for x in range(9):
        for y in range(9):
            if len(possibilities[x][y])==1:
                puzzle[x][y]=possibilities[x][y][0]

print_puzzle(puzzle)
print_current_status(puzzle)
update_possibilities(puzzle)
update_puzzle()
print_puzzle(puzzle)
print_current_status(puzzle)
print(possibilities[5][1])
