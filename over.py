class A :
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):   
        if (self.a<other.a):
         return ("obj 1 is less than obj 2")
        else:
         return ("obj 1 is not less than obj 2")
    def __eq__(self, other):
        if (self.a == other.a):
         return ("both are equal")
        else:
         return ("not equal")
obj1 = A(2)
obj2 = A(3)
print ("values:",obj1.a,obj2.a)
print (obj1 < obj2)

obj3 = A(4)
obj4 = A (4)
print ("values:",obj3.a,obj4.a)
print (obj3 == obj4)