import MySQLdb as m
host='localhost'
username='root'
password='ids123'
database='Empl'
db_con=m.connect(host,username,password,database)
db_cur=db_con.cursor(m.cursors.DictCursor)
sql="select * from emptable"
db_cur.execute(sql)
data=db_cur.fetchall()
for row in data:
	print row['name']
#	for i in range(len(row)):
#		print i
