#read json file write employee data into new json file emp.json
import json
fp1=open("data.json",'r')
fp2=open("emp.json",'w')
employees=json.load(fp1)
json.dump(employees,fp2)
print("New Json File Created")

fp1.close()
fp2.close()