class const:
    def __init__(self,name,place,age):
        self.name=name
        self.place=place
        self.age=age
    def __str__(self):
        return str(self.age)

p1=const("Ocean","Pondy",20)
print(p1)        