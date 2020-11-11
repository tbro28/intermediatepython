class rect: 
	l=8 
	b=5
	def rectarea(self):
		return rect.l * rect.b
	def rectarea1(self):
		return rect.l * 12
r=rect()
print ("Area of rectangle is ", r.rectarea())
print ("Area of rectangle is ", r.rectarea1())
