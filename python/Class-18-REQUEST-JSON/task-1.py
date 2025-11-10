import requests

resp_data=requests.get('https://jsonplaceholder.typicode.com/users')
print(type(resp_data)) #<class 'requests.models.Response'>
users=resp_data.json()
print(type(users))     #<class,list>
print(resp_data.status_code)  #200

for user in users:
    print(user['username'])