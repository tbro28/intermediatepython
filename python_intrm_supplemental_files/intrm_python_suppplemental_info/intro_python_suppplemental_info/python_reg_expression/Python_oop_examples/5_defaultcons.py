class rect: 
	k=20
	def __init__(self,x,y):
		self.l = x
		self.b = y
	def rectarea(self):
		return self.l * self.b * rect.k ) 

r=rect(10,4)
r1=rect(20,5)
r2=rect(32,23)
d2=rect(10,23)
print(d2.rectarea())
