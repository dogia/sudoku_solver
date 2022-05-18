import copy
import time

COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']


def init():
    _sudoku = {}
    for c in COLUMNS:
        _sudoku[c] = {}
        for r in range(9):
            _sudoku[c][r] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return _sudoku


def draw(_sudoku):
    screen = ""
    for r in range(9):
        for c in COLUMNS:
            # screen += f"{c}{r}:"
            screen += f"{_sudoku[c][r]} "
        screen += "\n"
    return screen


def lock(_sudoku, column, row, value):
    # Ignore value = 0
    if value == 0:
        return _sudoku

    solved = isinstance(_sudoku[column][row], int)
    if not solved and not (value in _sudoku[column][row]):
        print(f"Cell [{column}{row}] can not be set to: {value}")
        exit(1)
    # Lock in row
    for r in range(9):
        solved = isinstance(_sudoku[column][r], int)
        if not solved and value in _sudoku[column][r]:
            _sudoku[column][r].remove(value)

    # Lock in column
    for c in COLUMNS:
        solved = isinstance(_sudoku[c][row], int)
        if not solved and value in _sudoku[c][row]:
            _sudoku[c][row].remove(value)

    # Lock in box
    square_column = int(COLUMNS.index(column) / 3) * 3
    square_row = int(row / 3) * 3

    for row_carry in range(3):
        r = square_row + row_carry
        for column_carry in range(3):
            c = COLUMNS[square_column + column_carry]

            solved = isinstance(_sudoku[c][r], int)
            if not solved and value in _sudoku[c][r]:
                _sudoku[c][r].remove(value)
    _sudoku[column][row] = value
    return _sudoku


def load(_sudoku, filename):
    f = open(filename, "r")
    for r in range(9):
        for c in COLUMNS:
            v = int(f.readline())
            _sudoku = lock(_sudoku, c, r, v)
    return _sudoku


def completed(_sudoku):
    for r in range(9):
        for c in COLUMNS:
            solved = isinstance(_sudoku[c][r], int)
            if not solved:
                return False
    return True


def impossible(_sudoku):
    for r in range(9):
        for c in COLUMNS:
            solved = isinstance(_sudoku[c][r], int)
            if not solved and len(_sudoku[c][r]) == 0:
                return True
    return False


def shortest(_sudoku):
    minimum = 9
    length = 9
    column = None
    row = None

    for r in range(9):
        for c in COLUMNS:
            solved = isinstance(_sudoku[c][r], int)
            if not solved and len(_sudoku[c][r]) < minimum:
                minimum = len(_sudoku[c][r])
                column = c
                row = r
    return {
        'column': column,
        'row': row,
        'length': length
    }


def backtrack(_sudoku):
    srt = shortest(_sudoku)
    c = srt['column']
    r = srt['row']

    for v in _sudoku[c][r]:
        tmp = copy.deepcopy(_sudoku)
        tmp = lock(tmp, c, r, v)

        if impossible(tmp):
            return False

        solve(tmp)


def solve(_sudoku):
    # Solve cells with only one solution
    for r in range(9):
        for c in COLUMNS:
            cell = _sudoku[c][r]
            solved = isinstance(cell, int)
            if not solved and len(cell) == 1:
                v = cell[0]
                _sudoku = lock(_sudoku, c, r, v)
                return solve(_sudoku)

    if completed(_sudoku):
        print(draw(_sudoku))
        return _sudoku

    # Once here we need to use backtracking
    backtrack(_sudoku)


# Sudoku has been taken from https://www.sudokumania.com.ar/juegos/sudoku
# veryeasy: SD1OVCNW
# easy: SD2POYFO
# medium.txt: SD3NCQXP
# hard: SD4CDQGU
# veryhard: SD5FEKLR
# superveryhard: SD6GAUMK
# Imposible: SD9FDOPM


t = time.time_ns()
sudoku = init()
sudoku = load(sudoku, "hard.txt")
solve(sudoku)

print(f"Solved in {time.time_ns() - t} ns")
