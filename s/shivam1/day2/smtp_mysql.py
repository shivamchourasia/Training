import sys
import smtplib
import getpass
import MySQLdb as m
host="smtp.gmail.com"
port=587
to=sys.argv[1]
database=sys.argv[2]#emp
db_con=m.connect('localhost','root','ids123',database)
db_cur=db_con.cursor(m.cursors.DictCursor)
server=smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
username="shivamchourasia190@gmail.com"
password=getpass.getpass()
server.login(username,password)
sub="database content"
db_cur.execute("select * from employee1")
data=db_cur.fetchall()
#with open('test.txt','r+')as f:
cont="\n"
for i in data:
	#print i.values()
	#f.write(str(i.values())+'\n')
	#mes=f.read()
	mes=i.values()	
	#cont = cont + "%d  %s  %s"%(mes[0],mes[1],mes[2]) +"\n"
	cont=cont+'{} {} {}'.format(mes[0],mes[1],mes[2])+"\n"
print cont

message="subject: %s\n\n%s"%(sub,cont)
server.sendmail(username,to,message)

