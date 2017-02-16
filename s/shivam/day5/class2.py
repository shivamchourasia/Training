class A:
	def __init__(self,a):
		self.a=a
	def __add__(self,other):
		return self.a+other.a
	def __sub__(self,other):
		return self.a-other.a
e=A(10)
f=A(20)
#c=A(30)
print e+f
print e-f
#v=__sub__()
#print v
