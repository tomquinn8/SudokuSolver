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
    #Solved/Unsolved
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

print_puzzle(puzzle)
print_current_status(puzzle)
