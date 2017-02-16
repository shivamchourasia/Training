import MySQLdb as m
import sys
import smtplib
import getpass
host='localhost'
username='root'
password='ids123'
database='Empl'
lis=[]
db_con=m.connect(host,username,password,database)
db_cur=db_con.cursor(m.cursors.DictCursor)
to=sys.argv[1]
a=sys.argv[2]
sql="select * from a"
db_cur.execute(sql)
data=db_cur.fetchall()
for row in data:
	lis.append(row)
with open('t.txt','w')as f:
	f.write(lis)
host="smtp.gmail.com"
port=587
server=smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
username='shivamchourasia190@gmail.com'
password=getpass.getpass()
server.login(username,password)

sub=a
mes=t.txt
message="subject:  %s\n\n %s"%(sub,mes)
server.sendmail(username,to,message)
