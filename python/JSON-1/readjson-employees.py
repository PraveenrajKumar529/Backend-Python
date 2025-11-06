#read json file and print data
#read json file and print all employee names
import json 
fp=open('data.json','r')
employees=json.load(fp)
print(type(employees))

for emp in employees:
    print(emp['ename'])