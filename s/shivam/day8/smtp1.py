import sys
import smtplib
import getpass
host="smtp.gmail.com"
port=587
server=smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
username='shivamchourasia190@gmail.com'
password=getpass.getpass()
server.login(username,password)
to=sys.argv[1]
sub=sys.argv[3]
mes=sys.argv[2]
with open(mes,'r')as f:
	f1=f.read()
	message="subject:  %s\n\n %s"%(sub,f1)
	server.sendmail(username,to,message)
