""" How to invoke Rest API?
how to handle Json file?
what is json?
how to handle csv files?
csv vs json format?
how to handle file with path? """
import requests,json,csv
fp1=open("emp.json","w")
fp2=open("emp.csv","w",newline="")
#extract data from rest api?
user_resp=requests.get("https://jsonplaceholder.typicode.com/users")
users=user_resp.json()
print(users)