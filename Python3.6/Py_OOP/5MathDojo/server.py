class MathDojo(object):
    def __init__(self, number = 0):
        self.value = 0
        
    def add(self, *args):
        for arg in args:
            if type(arg) is list or type(arg) is tuple:
                for val in arg:
                    self.value += val
            else:
                self.value += arg
        return self

    def subtract(self, *args):
        for arg in args:
            if type(arg) is list or type(arg) is tuple:
                for val in arg:
                    self.value -= val
            else:
                self.value -= arg
        return self

    def result(self):
        print (self.value)

md = MathDojo()

x = md.add(2).add(2,5,1).subtract(3,2).result() #OUTPUTS 5

