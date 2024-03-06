class Point:
    def __init__(self,x,y):
        print("init called")
        self.x=x
        self.y=y
    def __str__(self):
        print("str called")
        return "({0},{1})".format(self.x,self.y)
    def __add__(self,obj):
                print("add called")
                x=self.x+obj.x
                y=self.y+obj.y
                return Point(x,y)
p1=Point(10,22)
print(p1)
p2=Point(20,22)
print(p2)
print("Addition of Object :",p1+p2)
