import pickle
import re
v=raw_input("mysql>")
s=raw_input("mysql>")
p=re.match("create",s,re.I)
if p:
	s1=re.findall(r'\((.*?)\)',s)
	s1=s1.split(",")
	for i in s1:create table
		pickle.dump(i,indent=0)
