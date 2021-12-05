class Student:
    def __init__(self,name):
        self.name = name
class Marks(Student):
    def __init__(self,mark,name):
        super().__init__(input("Enter name:"))
        self.mark = mark
        print(self.name ,"marks is ",self.mark)
m1 = Marks(78,"ocean")
        
        
