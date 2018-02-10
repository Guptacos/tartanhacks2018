import math
import sys
import os
sys.path.append(os.path.abspath("qm_files/"))
from qm import *

def getMin(ones):
    print(ones)
    qmOutput = qm(ones) #get minimized qm function from library
    print(qmOutput)
    equation = convert(qmOutput)    #convert library output to work with eval
    print(equation)
    return equation

def convert(qm):
    #if the equation is always true return 1
    if len(qm) == 0 or len(qm[0]) == 0: return "1"
   
    #note that the variable qm, returned from the library qm function, is of the
    #form of a list of strings. In each string, the leftmost term represents A,
    #then B, and so on. 1 = A, 0 = not A, and X = don't care. This is used below
    #to transform the list into a visually readable equation that can also be 
    #used with eval if the variables are replaced with ones and zeros.
    eq = ""
    for product in qm:
        eq += "("
        numOp = len(product)
        count = 0
        while count < numOp:
            val = product[count]
            if count == 0:
                if val == '1': eq += "A"
                elif val == '0': eq += "(not A)"
            elif count == 1:
                if val == '1': eq += "B"
                elif val == '0': eq += "(not B)"
            elif count == 2:
                if val == '1': eq += "C"
                elif val == '0': eq += "(not C)"
            elif count == 3:
                if val == '1': eq += "D"
                elif val == '0': eq += "(not D)"
        
            if val != "X": eq += " & "
            count += 1
        eq = eq[0 : -3] #after completing, remove the last &
        eq += ") | "
    eq = eq[0 : -3]
    return eq
