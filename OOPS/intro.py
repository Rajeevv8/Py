#Class def

class demo:
    attr1="You called attr1"
#Fn def needs self since object needs a place to sit when created
    def fn1(self):
        print("You called fn1")

#To instantiate an object
o1=demo()

#To call class attribute or function using object
print(o1.attr1)
o1.fn1()