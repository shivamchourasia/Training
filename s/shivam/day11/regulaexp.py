import re
str1=raw_input("enter")
#l=[]
#s1=str1.split(",")
#for i in s1:
s=re.findall(r'\d+\w+',str1)
print s
