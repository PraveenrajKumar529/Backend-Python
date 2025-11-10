import requests,json,csv 
fp1=open("user.json",'w')
fp2=open('user.csv','w',newline="")
#Extract Data from Rest API
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

#Load into 
#a)CSV File  b)JSON File
cw_obj=csv.writer(fp2)
cw_obj.writerow(["uid","unmae","email","city"])
cw_obj.writerows(user_csv_data)
print("New CSV File Created Successfully")

#Load into json file
json.dump(user_json_data,fp1)
print("New JSON file Created")


fp1.close()
fp2.close()