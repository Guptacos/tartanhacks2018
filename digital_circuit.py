from equation_parse import *
from ourQM import *

class Circuit(object):
    def __init__(self,in1,in2,image=None):
        self.in1=in1
        self.in2=in2
        self.userEq = self.get_user_eq()
        self.truthTable = None
        self.qm = None
        self.image=image

    def __repr__(self):
        return self.userEq

    def get_table(self):
        if self.truthTable == None:
            self.truthTable = make_truth_table(self.userEq)
        return self.truthTable

    def get_qm(self):
        if self.qm == None:
<<<<<<< HEAD
            self.qm = get_min(self.get_table())
=======
            self.qm = getMin(self.get_table())
>>>>>>> 6294d40f84af9f332d5361f3d9b674581109e32f
        return self.qm

    def get_user_eq(self):
        raise Exception("""You forgot to define get_user_eq in a child function 
                        you goon""")

class CInput(object):
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return self.name
