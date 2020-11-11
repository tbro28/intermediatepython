class rect: 
	def __init__(self, x=10,y=30):
		self.l = x
		self.b = y
	def rectarea(self):
		return self.l * self*b
r=rect(5,8)
print ("Area of rectangle is ", r.rectarea())
r=rect()
print ("Area of rectangle is ", r.rectarea())
r=rect(5)
print ("Area of rectangle is ", r.rectarea(10,20))
r=rect(y=5)
print ("Area of rectangle is ", r.rectarea(10,20))
