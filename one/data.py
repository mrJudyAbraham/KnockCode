import sqlite3
import one.validate
import one.ui
#conn=sqlite3.connect("knock.db")
#cr=conn.cursor()
#conn.execute('''create table details(id number,hash float);''')


def stor(ls=[],*a):
	conn=sqlite3.connect("knock.db")
	cr=conn.cursor()
	print("========================== KNOCK ENCODED ===========================")
	s=0
	for i in ls:
		s*=100
		s+=i
	print(s)
	k=1
	q="insert into details(id,hash) values (?,?);"
	cr.execute(q,(k,s))
	conn.commit()
	cr.close()
	conn.close()
	print("========================== KNOCK  STORED ===========================")

def check(ls=[],*a):
	conn=sqlite3.connect("knock.db")
	cr=conn.cursor()
	print("========================== CHECK INITIATED ===========================")
	s=0
	for i in ls:
		s*=100
		s+=i
	print(s)
	cr.execute("select hash from details")
	h=cr.fetchall()
	a=h[0]
	b=int(a[0])
	print(b)
	c=one.validate.evaluate(s,b)
	if(c==1):
		print("============================ AUTHENTICATED =============================")
		one.ui.inputs.alert(c)
	else:
		print("========================== NOT AUTHENTICATED ===========================")
		one.ui.inputs.alert(c)


