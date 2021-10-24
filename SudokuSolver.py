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
print_puzzle(puzzle)
