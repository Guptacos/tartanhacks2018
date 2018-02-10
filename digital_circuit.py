class circuit(object):
    def __init__(self,in1,in2):
        self.in1=in1
        self.in2=in2

class input(object):
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return self.name