from digital_circuit import *

class AndGate(circuit):
    def get_formula(self):
        return ("(%s & %s)" % (self.in1,self.in2))

    def __repr__(self):
        return self.get_formula()

class OrGate(circuit):
    def get_formula(self):
        return ("(%s | %s)" % (self.in1,self.in2))

    def __repr__(self):
        return self.get_formula()

class XorGate(circuit):
    def get_formula(self):
        return ("(%s ^ %s)" % (self.in1,self.in2))

    def __repr__(self):
        return self.get_formula()
        
class NotGate(circuit):
    def __init__(self,in1):
        self.in1=in1

    def get_formula(self):
        return ("(not %s)" % (self.in1))

    def __repr__(self):
        return self.get_formula()
        
class NandGate(circuit):
    def get_formula(self):
        return ("(not (%s & %s))" % (self.in1,self.in2))

    def __repr__(self):
        return self.get_formula()
        
class NorGate(circuit):
    def get_formula(self):
        return ("(not (%s | %s))" % (self.in1,self.in2))

    def __repr__(self):
        return self.get_formula()
        
A=input('A')
B=input('B')
cir1=AndGate(A,B)
cir2=OrGate(A,cir1)
cir3=NotGate(B)
cir4=NandGate(cir3,cir2)
print(cir4.get_formula())