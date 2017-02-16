import pexpect
import sys
m=pexpect.spawn("python arithmetic_pexpect.py")
m.logfile_read=sys.stdout
m.expect("var1")
#var1=input("enter")
m.sendline('8')
m.expect("var2")
#var2=input("enter")
m.sendline('9')
m.expect("var3")
#var3=raw_input("op")
m.sendline('-')
m.expect('\n')
m.close()
