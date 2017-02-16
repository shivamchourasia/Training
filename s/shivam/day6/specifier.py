class Shape:
	def __init__(self):
		print "shape"
	def e():
		print 'hello'
class Rectangle(Shape):
	def __init__(self,l,b):
		self.l=l
		self.b=b
		self.__c=self.l+self.b
a=Rectangle(2,3)
print a._Rectangle__c
b=Shape()
#print b._Rectangle__c
a.e()
