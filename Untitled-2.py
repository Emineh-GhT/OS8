class time:
    def __init__(self,h=0,m=0,s=0):
        self.h=h
        self.m=m
        self.s=s
        self.fix()
    def show(self):
        print(self.h,":",self.m,":",self.s)
    def fix(self):
        if self.s>= 60:
            self.s-=60
            self.m+=1
        elif self.s<0:
            self.m=self.m-1
            self.s=self.s+60
        if self.m>= 60:
            self.m-=60
            self.h+=1
        elif self.m<0:
            self.h=self.h-1
            self.m=self.m+60
    def sum_t(self,other):
        result=time()
        result.h=self.h+other.h
        result.m=self.m+other.m
        result.s=self.s+other.s
        result.fix()
        return result
    def sub_t(self,other):
        result=time()
        result.h=self.h-other.h
        result.m=self.m-other.m
        result.s=self.s-other.s
        result.fix()
        return result
def menu():
    print("1) jam | 2) tafriq | 3) sanye ba zaman | 4) zaman be sanye | 5) Exit")
def voroodi():
    h1=int(input("saat :"))
    m1=int(input("daqiqe :"))
    s1=int(input("sanye :"))
    t=time(h1,m1,s1)
    return t
def sanye_zaman(x):
    m=0
    h=0
    if x>60:
        r=x//60
        x=x-r* 60
        m+=r
        if m>60:
            r=m//60
            m=m-r* 60
            h+=r
    print("sanye be zaman:  ",h,":",m,":",x)
def zaman_sanye():
    print("saat:")
    h=int(input())
    print("daqiqe:")
    m=int(input())
    print("sanye:")
    s=int(input())
    m=m+h*60
    s=s+m*60
    print("zaman be sanye:",s)
while True:
    menu()
    c=int(input())
    if c==1:
        t1=voroodi()
        t2=voroodi()
        a=t1.sum_t(t2)
        a.show()
    elif c==2:
        t1=voroodi()
        t2=voroodi()
        b=t1.sub_t(t2)
        b.show()
    elif c==3:
        print("tabdil zaman be seconds:")
        x=int(input())
        sanye_zaman(x)
    elif c==4:
        zaman_sanye()
    elif c==5:
        break