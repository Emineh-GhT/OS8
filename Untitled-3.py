
class adad:
    def __init__(self,n=0,i=0):
        self.n=n
        self.i=i
    def show(self):
        if self.i==0:
            print(self.n)
        else:
            print(self.n,end="+")
            print("( ",self.i,end="i )")
    def jam(self,other):
        result=adad()
        result.n=self.n+other.n
        result.i=self.i+other.i
        return result
    def tafriq(self,other):
        result=adad()
        result.n=self.n-other.n
        result.i=self.i-other.i
        return result
    def zarb(self,other):
        result=adad()
        result.n=self.n*other.n
        result.i=self.i*other.n + other.i*self.n
        return result
x1=int(input("X1 : "))
y1=int(input("Y1 : "))
a=adad(x1,y1)
x2=int(input("X2 : "))
y2=int(input("Y2 : "))
b=adad(x2,y2)
d=a.jam(b)
print("\n jam: ")
d.show()
e=a.tafriq(b)
print("\n tafriq: ")
e.show()
f=a.zarb(b)
print("\n zarb: ")
f.show()
print ("\n")
 