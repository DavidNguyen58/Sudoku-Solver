# Data will be communicated via JSON index 1
from sat import dpll_sat_solve

def encode_sudoku():
    # Encode the problem using propostional logic, return a list of lists
    # Introducing a variable x_r,c,v. The row r, column c will take value of v.
    # The formula consists of 6 different clauses encoding different aspects of the game
    ...


def decode_sudoku(sol):
    # Decode the problem to readable data
    res = {}
    for var in sol:
        key = str(var)[0:2]
        v = str(var)[2]
        res[key] = v
    return res


def clause_one():
    # Each entry has at least one value
    cls = []
    for r in range(1, 10):
        for c in range(1, 10):
            tmp = [int(f'{r}{c}{v}') for v in range(1, 10)]
            cls.append(tmp)
    return cls


def clause_two():
    cls = []
    for r in range(1, 10):
        for c in range(1, 10):
            for v in range(1, 10):
                for n in range(v + 1, 10):
                    x = f'-{r}{c}{v}'
                    y = f'-{r}{c}{n}'
                    cls.append([int(x), int(y)])
    return cls

def clause_three():
    # Each row has all the numbers
    cls = []
    for r in range(1, 10):
        for v in range(1, 10):
            tmp = [int(f'{r}{c}{v}') for c in range(1, 10)]
            cls.append(tmp)
    return cls

def clause_four():
    # Each column has all the numbers
    cls = []
    for c in range(1, 10):
        for v in range(1, 10):
            tmp = [int(f'{c}{r}{v}') for r in range(1, 10)]
            cls.append(tmp)
    return cls

def clause_five():
    # Each 3x3 subgrid contains all the numbers from 1 to 9
    cls = []
    for n in range(1, 10):
        for r in range(0, 3):
            for c in range(0, 3):
                tmp = []
                for i in range(1, 4):
                    for j in range(1, 4):
                        a = 3*r + i
                        b = 3*c + j
                        tmp.append(int(f'{a}{b}{n}'))
                cls.append(tmp)
    return cls


def clause_six(data):
    # The solution with respects the given clues
    cls = []
    for key in data:
        if data[key] != '':
            cls.append(int(f"{key}{data[key]}"))
    return cls


