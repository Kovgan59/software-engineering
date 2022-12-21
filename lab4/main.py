class A:
    def __init__(self, a):
        self.a = a
 
    # adding two objects
    def __add__(self, o):
        return self.a + o.a * 3
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")
 
print(ob1 + ob2)
print(ob3 + ob4)
# Actual working when Binary Operator is used.
print(A.__add__(ob1 , ob2))
print(A.__add__(ob3,ob4))
#And can also be Understand as :
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))

    # def___sub__

    # def__mul__
    
    # def__truediv__
