from digital_circuit import *
from gates import *

colMax = 7
rowMax = 5

def get_circuit(grid):      #grid is a 2d list
    rowNum = 0
    colNum = colMax
    err = ""
    circuit = None
    while True:     #finds rightmost output gate
        val = grid[rowNum][colNum]
        if val != None: break
        rowNum += 1
        
        if rowNum > rowMax:
            rowNum = 0
            colNum -= 1
        if colNum < 0: err = "No gates found!"
    
    #at this point, rowNum and rowCol are the coordinates of the output val
    #now we have to check that there are no gates in the same row as the output
    if err == "":
        curCol = get_col(grid, colNum)
        for index in range(rowMax + 1):
            if index == rowNum: continue
            elif curCol[index] != None: 
                err = "Can't have multiple outputs!"
        
    if err == "":
        (circuit, err) = create_elem(grid, val, rowNum, colNum)
        #check that every circuit element has been used
        #for row in grid:
        #    if not is_empty(row):
        #        invalid_circuit("parts of circuit disconnected")
    return (circuit, err)

def create_elem(grid, val, curRow, curCol):
    err = ""

    if val == "A": return (CInput("A"), err)
    elif val == "B": return (CInput("B"), err)
    elif val == "C": return (CInput("C"), err)
    elif val == "D": return (CInput("D"), err) #base cases
    
    else:
        if curCol == 0:
            err = "Can't have gate on left edge of board."
        if err == "":
            ((in1, in2, row1, row2), err) = get_closest(grid,curRow,curCol)
        if err == "":
            (circ1, err) = create_elem(grid, in1, row1, curCol-1)
        if err == "":
            (circ2, err) = create_elem(grid, in2, row2, curCol-1)
        if err == "":
            if val == "and": return (AndGate(circ1, circ2), err)
            elif val == "or": return (OrGate(circ1, circ2), err)
            elif val == "xor": return (XorGate(circ1, circ2), err)
            elif val == "not": return (NotGate(circ1), err) #circ1 == circ2 
    #if you reach this part of the code, that means you hit an error. Return err
    return (None, err)

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
    err = ""
    if col == 0: err = "Oops! your gate was too far left."
    
    if err == "":
        colPrev = get_col(grid, col-1)

    if err == "":
        if col%2 == 0:      #case where offset of our grid is relevant
            if ((row == 0 and colPrev[row] == None) or
               (row == rowMax and colPrev[row-1] == None)): 
                err = "Uh oh! Your gate didn't have an input."
            elif row == 0: return ((colPrev[row], colPrev[row], row, row), err)
            elif row == rowMax: return ((colPrev[row-1], colPrev[row-1], row-1,row-1), err)
    if err == "":
        return (check_behind(grid, row, col), err)
    return (None, None, None, None, err)
        
def check_behind(grid, row, col):
    colPrev = get_col(grid, col-1)
    (val1, row1) = (colPrev[row-1], row-1) if (col%2 == 0) else (colPrev[row], row)
    (val2, row2) = (colPrev[row], row) if (col%2 == 0) else (colPrev[row+1], row+1)
    
    if (val1 != None and val2 != None): return (val1, val2, row1, row2)
    elif (val1 == None): return (val2, val2, row2, row2)
    else: return (val1, val1, row1, row1)
