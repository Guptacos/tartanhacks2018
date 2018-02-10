def parse_equation(A,B,C,D,equation):
    newStr = ''
    truthVals = {'A','B','C','D'}
    for c in equation:
        if (c not in truthVals):
            newStr += c
        else:
            if (c == 'A'):
                newStr += str(A)
            elif (c == 'B'):
                newStr += str(B)
            elif (c == 'C'):
                newStr += str(C)
            elif (c =='D'):
                newStr += str(D)

    return eval(newStr)

# print(parse_equation(True,False,True,True,"(A ^ B)"))

def make_truth_table(equation):
    table = [False]*16
    for address in range(16):
        #000..00DCBA
        A = bool(address & 1)
        B = bool(address>>1 & 1)
        C = bool(address>>2 & 1)
        D = bool(address>>3 & 1)
        table[address] = parse_equation(A,B,C,D,equation)

    return table 

print(make_truth_table("((A ^ B) ^ (C ^ D))"))
