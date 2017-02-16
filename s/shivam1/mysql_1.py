import MySQLdb as m
db_con=m.connect('localhost','root','ids123','emp')
db_cur=db_con.cursor(m.cursors.DictCursor)
#db_cur.execute("""create table employee1(id varchar(10),name varchar(20),age int)""")
#db_cur.execute("""insert into employee1(id,name,age) values('6172','shivam',23)""")
#db_con.commit()
db_cur.execute("select * from employee1")
data=db_cur.fetchall()
with open('test.txt','w+')as f:
	for i in data:
		print i.values()
		f.write(str(i.values())+'\n')

