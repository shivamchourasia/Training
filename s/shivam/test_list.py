var=int(raw_input("enter the no."))
lis_value=['Jan,Feb,Mar','Apr,May,Jun','Jul,Aug,Sep','oct,Nov,Dec']
l1=lis_value[var-1].split(",")
for i in l1:
	print i
