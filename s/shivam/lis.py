lis=[]
l=input("enter the range")
for i in range(l):
	var1=input("enter the number:")
	lis.append(var1)
for i in range(l):
	for j in range(l):
		if lis[i]>lis[j]:
			temp=lis[i]
			lis[i]=lis[j]
			lis[j]=temp
print lis[1]
