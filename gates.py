from digital_circuit import *

class AndGate(Circuit):
    def get_user_eq(self):
        return ("(%s & %s)" % (self.in1,self.in2))

class OrGate(Circuit):
    def get_user_eq(self):
        return ("(%s | %s)" % (self.in1,self.in2))

class XorGate(Circuit):
    def get_user_eq(self):
        return ("(%s ^ %s)" % (self.in1,self.in2))
        
class NotGate(Circuit):
    def __init__(self,in1,image=None):
        super().__init__(in1,None,image)

    def get_user_eq(self):
        return ("(not %s)" % (self.in1))

class NandGate(Circuit):
    def get_user_eq(self):
        return ("(not (%s & %s))" % (self.in1,self.in2))

class NorGate(Circuit):
    def get_user_eq(self):
        return ("(not (%s | %s))" % (self.in1,self.in2))

# A=Input('A')
# B=Input('B')
# cir1=AndGate(A,B)
# cir2=OrGate(A,cir1)
# cir3=NotGate(B)
# cir4=NandGate(cir3,cir2)
# print(cir4.get_user_eq())
