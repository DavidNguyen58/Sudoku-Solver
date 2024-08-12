import json
from pysat.solvers import Solver

# Data will be communicated via JSON index 1
def encode_sudoku(data):
    # Encode the problem using propostional logic, return a list of lists
    # Introducing a variable x_r,c,v. The row r, column c will take value of v.
    # The formula consists of 6 different clauses encoding different aspects of the game
    tmp = clause_six(data)
    if tmp == None:
        return None
    cnf = clause_one() + clause_two() + clause_three() + clause_four() + clause_five() + tmp
    return cnf

def solve_sudoku(cnf):
    solver = Solver(name="mcb")
    if cnf == None:
        return None
    for cls in cnf:
        solver.add_clause(cls)
    if solver.solve():
        return solver.get_model()
    return None

def decode_sudoku(sol):
    # Decode the problem to readable data
    res = {}
    if sol == None:
        return None
    for var in sol:
        if 111 <= var and var <= 999:
            key = str(var)[0:2]
            v = str(var)[2]
            res[key] = v
    # return as a JSON string
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
    # Each cell contains at most 1 number
    cls = []
    for r in range(1, 10):
        for c in range(1, 10):
            for i in range(1, 10):
                for j in range(i + 1, 10):
                    x = f'-{r}{c}{i}'
                    y = f'-{r}{c}{j}'
                    cls.append([int(x), int(y)])
    return cls

def clause_three():
    # Each row has all the numbers
    cls = []
    for r in range(1, 10):
        for v in range(1, 10):
            tmp = [int(f'{r}{c}{v}') for c in range(1, 10)]
            cls.append(tmp)
    # Each row must contain all distinct integers
    """
    for r in range(1, 10):
        for v in range(1, 10):
            for i in range(1, 10):
                for j in range(i + 1, 10):
                    x = f'-{r}{i}{v}'
                    y = f'-{r}{j}{v}'
                    cls.append([int(x), int(y)])
    """
    return cls

def clause_four():
    # Each column has all the numbers
    cls = []
    for c in range(1, 10):
        for v in range(1, 10):
            tmp = [int(f'{r}{c}{v}') for r in range(1, 10)]
            cls.append(tmp)
    # Each column must contain all distinct integers
    """
    for c in range(1, 10):
        for v in range(1, 10):
            for i in range(1, 10):
                for j in range(i + 1, 10):
                    x = f'-{i}{c}{v}'
                    y = f'-{j}{c}{v}'
                    cls.append([int(x), int(y)])
    """
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
    # Each subgrid contains all the distinct numbers
    return cls

def clause_six(data):
    # The solution with respects the given clues
    # Data will be stored in a Python dictionary
    cls = []
    count = 0
    for key in data:
        if data[key] != '':
            count += 1
            cls.append([int(f"{key}{data[key]}")])
    # Sudoku problem is only solvable if there is 17 clues on the board
    if count < 17:
        return None
    return cls




