from equation_parse import *

def parse_truth_table(table): #generate list of minterms
    zeroOnes  = []
    oneOnes   = []
    twoOnes   = []
    threeOnes = []
    fourOnes  = []

    for row in range(16):
        if table[row]:
            count = bin(row).count('1')
            #print(count)
            if count == 0:
                zeroOnes.append(row)
            elif count == 1:
                oneOnes.append(row)
            elif count == 2:
                twoOnes.append(row)
            elif count == 3:
                threeOnes.append(row)
            else:
                fourOnes.append(row)

    return [zeroOnes,oneOnes,twoOnes,threeOnes,fourOnes]


def find_prime_implicants(minTerms):
    





# parse_truth_table(make_truth_table("((A ^ B) ^ (C ^ D))"))