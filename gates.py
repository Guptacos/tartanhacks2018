from digital_circuit import *

class AndGate(circuit):
    def get_user_eq(self):
        return ("(%s & %s)" % (self.in1,self.in2))

class OrGate(circuit):
    def get_user_eq(self):
        return ("(%s | %s)" % (self.in1,self.in2))

class XorGate(circuit):
    def get_user_eq(self):
        return ("(%s ^ %s)" % (self.in1,self.in2))
        
class NotGate(circuit):
    def __init__(self,in1):
        super().__init__(in1,None)

    def get_user_eq(self):
        return ("(not %s)" % (self.in1))

class NandGate(circuit):
    def get_user_eq(self):
        return ("(not (%s & %s))" % (self.in1,self.in2))

class NorGate(circuit):
    def get_user_eq(self):
        return ("(not (%s | %s))" % (self.in1,self.in2))

A=input('A')
B=input('B')
cir1=AndGate(A,B)
cir2=OrGate(A,cir1)
cir3=NotGate(B)
cir4=NandGate(cir3,cir2)
print(cir4.get_user_eq())
