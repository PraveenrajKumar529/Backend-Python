import mysql.connector
dbcon=None 
cursor=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='db4') 
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='''
           insert into employees(eid,ename,email,city) values(%s,%s,%s,%s);
           '''
    employees=[
        (102,'sonia','sg@gmail.com','ND'),
        (103,'Priya','priya@gmail.com','Bangalore'),
        (104,'Modi','md@gmail.com','Bangalore'),
        (105,'Amith','amith@gmail.com','ND'),
        (106,'VS','vs@gmail.com','ND'),
    ]
    cursor.executemany(sql_st,employees)
    dbcon.commit()
    print("Data Inserted Successfully!")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()