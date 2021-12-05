class A:
    def __init__(self):
        print("A is a class")
class B(A):
    def __init__(self):
        
        print("B is also a class")
        super().__init__()
       


#Single A-->B
#Multilevel A-->B-->C
#Multiple 

class A:
    def clsA(self):
        print("This is A")
class B(A):
    def clsB(self):
        print("This is B") 
class C(B):
    def clsC(self):
        print("This is C")

obj=C()
obj.clsB()                       