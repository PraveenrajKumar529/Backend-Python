import requests,json,csv,mysql.connector
fp1=open("user.json","w")
fp2=open('user.csv','w',newline="")
user_resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=user_resp.json()
#Transform for CSV File and json file
user_csv_data=[]
user_json_data=[]
for user in users:
    user_csv_data.append((user['id'],
                          user['username'],
                          user['email'],
                          user['address']['city']))
    user_json_data.append({"uid":user['id'],
                           "uname":user['username'],
                           "email":user['email'],
                           "city":user['address']['city']})
json.dump(user_json_data,fp1)
print("New Json File is Created")

cw_obj=csv.writer(fp2)
cw_obj.writerow(["uid","uname","email","city"])
cw_obj.writerows(user_csv_data)
print("New CSV File Created Successfully")

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
            create table users(
            uid int,
            uname varchar(32),
            uemail varchar(32),
            ucity varchar(32)
            );
            '''
    sql_st1='''
            insert into users(uid,uname,uemail,ucity) values(%s,%s,%s,%s)
            '''
    cursor.execute(sql_st)
    cursor.executemany(sql_st1,user_csv_data)
    dbcon.commit()
    print("SQL TABLE CREATED Successfully!")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()