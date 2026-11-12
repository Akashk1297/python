class Car:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    # no arguments as input
    def myfunc1(self):
        # return tuple
        return (self.name,self.id)

    # 2 args input
    def myfunc2(self,var1,var2):
        #tuple
        return (var1,var2)

obj1=Car("akash",1)
resp1=obj1.myfunc1()
resp2=obj1.myfunc2(5,6)
print(resp1)
print(resp2)
