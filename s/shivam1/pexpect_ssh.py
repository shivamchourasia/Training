from pexpect import pxssh
#import getpass
try:
	s=pxssh.pxssh()
	s.login("192.168.0.41","ids","ids123")
	s.sendline("ls-l")
	s.prompt()
	print(s.before)
	s.logout()
except pxssh.ExceptionPxssh,e:
	#print str(e)
	print 'wrong'
