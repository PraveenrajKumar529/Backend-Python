import requests,json
fp=open("users.json",'w')
resp_data=requests.get("https://jsonplaceholder.typicode.com/users")
users=resp_data.json()

with open("user.json",'w')as fp:
    json.dump(users,fp)
print("New File Created sucessfully")