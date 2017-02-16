import MySQLdb as m
db_con=m.connect('localhost','root','ids123','emp')
db_cur=db_con.cursor(m.cursors.DictCursor)
db_cur.execute("""create table employee(id varchar(10),name varchar(20),age int,primary key(id))""")
db_cur.execute("""insert into employee(id,name,age)values('6172','shivam',23)""")
data=db_cur.fetchall()
for i in data:
	print i 
