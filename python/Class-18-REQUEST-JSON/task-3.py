import csv
fp=open("emp.csv","w")
cw=csv.writer(fp)
cw.writerow(["eid","ename","esal"])
data=[
    (101,"RG",45000)
    (102,"SG",55000)
    (103,"PG",65000)
]
cw.writerow(data)
print("sucess")
fp.close()