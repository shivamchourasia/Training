class A:
	def __init__(self,array):
		self.array=array
		lis=[]
		for i in range(3):
			row=[]
			for j in range(3):
				v=input("enter")
				row.append(v)
			lis.append(row)
	def __add__(self,other):
		return self.lis+other.lis
a=A()
b=A()
print a+b
