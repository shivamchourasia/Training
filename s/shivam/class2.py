class A:
	def __init__(self,a):
		self.a=a
	def __add__(self,other):
		return self.a+other.a
	def __sub__(self,other):
		return self.a-other.a
a=A(10)
b=A(20)
#c=A(30)
print a+b
print a-b
