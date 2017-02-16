import sys
try:
	v=sys.argv[1]
	f=file(v,"r")
#for i in range(2):
#	s=raw_input("enter")
#	f.write(s+"\n")
#f=file("file_test.txt","r")
	t1=f.read();
	print t1
	t1=t1.split("\n")
	t2= [ x.split(" ") for x in t1]
	for x in t2:
		try:
			print x[1]
		except:
			pass
	f.close()
except:
	print("wrong filename")
