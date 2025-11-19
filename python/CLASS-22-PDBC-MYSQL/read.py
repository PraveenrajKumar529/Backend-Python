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
           SELECT *FROM EMPLOYEES
           '''
    cursor.execute(sql_st)
    employees=cursor.fetchall();
    #print(employees)
    for emp in employees:
        print(emp[1])
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()