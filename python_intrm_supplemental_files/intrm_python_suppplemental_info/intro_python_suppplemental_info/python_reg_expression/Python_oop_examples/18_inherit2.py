from __future__ import division

class rect: 
	def __init__(self):
		self.l = 8
		self.b = 5
	def area(self):
		print ("Area of rectangle is ", self.l * self.b)

class triangle(rect): 

	def __init__(self):
		rect.__init__(self)
		self.x = 17
		self.y = 13
	def area(self):
		rect.area(self)
		print ("Area of triangle is ", 1/2*self.x * self.y)
	
r1=rect()
r1.area()
r=triangle()
r.area()
