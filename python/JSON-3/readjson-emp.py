import json 
fp=open('data.json','r')
employees=json.load(fp)

print(len(employees))    #5
print(type(employees))   #list

for emp in employees:
    if emp['avail']==True:
        print(emp['ename'])



fp.close()