import json
class Matrix:
	def __init__(self,array):
		self.array=array
	def __add__(self,other):
		if len(self.array)==len(other.array):
			new_matrix=[]
			for i in range(2):
				row=[]
				for j in range(2):
					row.append(self.array[i][j] + other.array[i][j])
				new_matrix.append(row)
			return Matrix(new_matrix)
		#	print new_matrix
	def __sub__(self,other):
		new_matrix=[]
		for i in range(2):
			row=[]
			for j in range(2):
				row.append(self.array[i][j] - other.array[i][j])
			new_matrix.append(row)
		return Matrix(new_matrix)
	def __str__(self):
		return str(self.array)
#	#	return json.dumps(self.array,indent=4)
l1=[]
for i in range(2):
	l2=[]
	for j in range(2):
		var=input("enter")
		l2.append(var)
	l1.append(l2)
l3=[]
for i in range(2):
	l4=[]
	for j in range(2):
		var=input("enter")
		l4.append(var)
	l3.append(l4)
a=Matrix(l1)
b=Matrix(l3)
print a
print b
print a+b
print a-b
