import pymysql

"""db = pymysql.connect("localhost","root","Lakki@58","test1" )

cursor=db .cursor()
sql=('select * from emp')
cursor.execute(sql)
data=cursor.fetchall()
print(data)





#db = pymysql.connect("localhost","root","Lakki@58","test1" )
#cursor = db.cursor()

#sql =  """insert into emp values (2,'ravi','reddy',28,'m',45000)"""

#try:
#    cursor.execute(sql)
#    db.commit()

#except:
#    db.rollback()

#db.close()



db = PyMySQL.connect("localhost","testuser","test123","TESTDB" )

cursor = db.cursor()

sql = "UPDATE EMPLOYEE SET AGE = AGE + 1
WHERE SEX = '%c'" % ('M')
try:
    cursor.execute(sql)

db.commit()
except:
    db.rollback()

db.close()"""






db = PyMySQL.connect("localhost","testuser","test123","TESTDB" )

cursor = db.cursor()
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
