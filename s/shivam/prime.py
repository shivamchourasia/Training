count=0
var=input("enter")
for i in range(var):
	if var%(i+1)==0:
		count=count+1
if count==2:
	print "it is  a prime"
else:
	print "its not a prime"	
