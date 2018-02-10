from digital_circuit import *
from gates import *

colMax = 7
rowMax = 5

def get_circuit(grid):      #grid is a 2d list
    output = None
    rowNum = 0
    colNum = colMax

    while True:     #finds rightmost output gate
        val = grid[rowNum][colNum]
        if val != None: 
            output = val
            break
        rowNum += 1
        if rowNum > rowMax:
            rowNum = 0
            colNum -= 1
        if colNum < 0: invalid_circuit("No gates found!")
    #at this point, rowNum and rowCol are the coordinates of the output val
    #now we have to check that there are no gates in the same row as the output
    grid[rowNum][colNum] = None
    curCol = get_col(grid, colNum)
    if not is_empty(curCol): invalid_circuit("Can't have multiple outputs!")
    
    print("output gate = ", rowNum, colNum, val)
    circuit = create_elem(grid, val, rowNum, colNum)
    #check that every circuit element has been used
    for row in grid:
        if not is_empty(row):
            print(row)
            print(circuit)
            invalid_circuit("parts of circuit disconnected")
    return circuit

def create_elem(grid, val, curRow, curCol):
    grid[curRow][curCol] = None
#    if val == None: raise Exception("Error: tried to create None gate")

    if val == "A": return CInput("A")
    elif val == "B": return CInput("B")
    elif val == "C": return CInput("C")
    elif val == "D": return CInput("D") #base cases
    
    else:
        if curCol ==0:
            print(curRow, curCol, val)
            invalid_circuit("Can't have gate on left edge of board.")
        print(curRow, curCol)
        (in1, in2, row1, row2) = get_closest(grid,curRow,curCol)
        circ1 = create_elem(grid, in1, row1, curCol-1)
        circ2 = create_elem(grid, in2, row2, curCol-1)
        if val == "and": return AndGate(circ1, circ2)
        elif val == "or": return OrGate(circ1, circ2)
        elif val == "xor": return XorGate(circ1, circ2)
        elif val == "not": return NotGate(circ1) #circ1 == circ2 if not gate
    #if you reach this part of the code, that means you hit an undefined gate
    print(val)
    raise Exception("Error: tried to create undefined gate")

def is_empty(row):
    for item in row:
        if item != None: return False
    return True

def get_row(grid, row):
    return grid[row]

def get_col(grid, col):
    result = []
    for row in grid:
        result.append(row[col])
    return result

def get_closest(grid, row, col):
    if col == 0: invalid_circuit("Oops! your gate was too far left.")
    colPrev = get_col(grid, col-1)

    if col%2 == 0:      #case where offset of our grid is relevant
        if ((row == 0 and colPrev[row] == None) or
           (row == rowMax and colPrev[row-1] == None)): 
            invalid_circuit("Uh oh! Your gate didn't have an input.")
        elif row == 0: return (colPrev[row], colPrev[row], row, row)
        elif row == rowMax: return (colPrev[row-1], colPrev[row-1], row-1,row-1)
    return check_behind(grid, row, col)
        
def check_behind(grid, row, col):
    colPrev = get_col(grid, col-1)
    (val1, row1) = (colPrev[row-1], row-1) if (col%2 == 0) else (colPrev[row], row)
    (val2, row2) = (colPrev[row], row) if (col%2 == 0) else (colPrev[row+1], row+1)
    print(val1, row1, val2, row2)
    if (val1 != None and val2 != None): return (val1, val2, row1, row2)
    elif (val1 == None): return (val2, val2, row2, row2)
    else: return (val1, val1, row1, row1)

def invalid_circuit(string):
    raise Exception(string)
