class circle(object):
        cnt=0
        def  __init__(self,x):
                self.r = x
                circle.cnt+=1
        def  carea(self):
                return self.r * self.r*3.14
        def  ccirf(self):
                return  2.0*3.14*self.r
        def  ccount(self):
                return  circle.cnt
        def  __str__(self):
                return str(self.r)


c1=circle(10.2)
print("c1 area = ",c1.carea())
print("c1 circumference = ",c1.ccirf())
print(c1)
c2=circle(12.2)
print("c1 area = ",c2.carea())
print("c1 circumference = ",c2.ccirf())
print(c2)
c3=circle(14.2)
print("c3 area = ",c3.carea())
print("c3 circumference = ",c3.ccirf())
print(c3)
print("circle count = ",c1.ccount())




