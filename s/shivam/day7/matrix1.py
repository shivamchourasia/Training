class A:
	def __init__(self):
		lis=[]
		for i in range(2):
			row=[]
			for j in range(2):
				v=input("enter")
				row.append(v)
			lis.append(row)
		#print lis
		lis1=[]
		for i1 in range(2):
			row1=[]
			for j1 in range(2):
				v1=input("enter")
				row1.append(v1)
			lis1.append(row1)
		#print lis1
		lis2=[]
		print lis
		print lis1
		for k in range(2):
			row2=[]
			for m in range(2):
				v=lis[k][m]+lis1[k][m]
				print row[m]
				print row1[m]
				row2.append(v)
			lis2.append(row2)
		print row
		print lis2
a=A()
