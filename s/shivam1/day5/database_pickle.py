import pickle
import re
v=raw_input("mysql>")
s=raw_input("mysql>")
l={}
p=re.match("create",s,re.I)
if p:
	s1=re.findall(r'\((.*?)\)',s)
	s=s.split(" ")
	print s[2]
	s2=s[2]
	s3=re.findall(r'^[^\(]+',s2)
	print s3
	with open('data.txt','w+')as f:
		pickle.dump(str(s3),f)
		for i in s1:
			pickle.dump(i,f)
			
		#s=pickle.load(f)
		#print s
		f.write("\n")	
