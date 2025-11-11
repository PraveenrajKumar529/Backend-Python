import mysql.connector
dbcon=None 
cursor=None
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='db4')
    cursor=dbcon.cursor()
    sql_st='''
            create table user(
            uid int,
            uname varchar(32)
            );
            '''
    cursor.execute(sql_st)
    print('New Mysql Table created Successfully') 
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()