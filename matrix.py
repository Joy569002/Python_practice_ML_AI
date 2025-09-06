

class Matrix:
    __slots__= ['a','b']
    def __init__(self, a: int, b:float):
        self.a=a
        self.b=b
    def seta(self,a:int):
        self.a=a
    def sete(self,b:float):
        self.b=b
    def geta(self):
        return self.a
    def getb(self):
        return self.b
    @classmethod
    def mult(cls,a:int,b:int):
        return cls(a*b,a+b)


p=Matrix.mult(10,12)
print(p.geta())
print(p.getb())