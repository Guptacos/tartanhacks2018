import math
import sys
import os
sys.path.append(os.path.abspath("qm_files/"))
from qm import *

def getfn(ones):
    qmOutput = qm(ones) #get minimized qm function from library
    equation = convert(qmOutput)    #convert library output to work with eval
    print(qmOutput)
    return equation

def convert(qm):
    #if the equation is always true return 1
    if len(qm) == 0 or len(qm[0]) == 0: return "1"
    
    eq = ""
    for product in qm:
        numOp = len(product)
        count = -1
        while abs(count) <= numOp:
            val = product[count]
            if abs(count) == 4:
                if val == '1': eq += "A"
                elif val == '0': eq += "(not A)"
            elif abs(count) == 3:
                if val == '1': eq += "B"
                elif val == '0': eq += "(not B)"
            elif abs(count) == 2:
                if val == '1': eq += "C"
                elif val == '0': eq += "(not C)"
            elif abs(count) == 1:
                if val == '1': eq += "D"
                elif val == '0': eq += "(not D)"
        
            if val != "X": eq += " & "
            count -= 1
        eq = eq[0 : -3]
        eq += " | "
    eq = eq[0 : -3]
    return eq
