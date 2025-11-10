import csv 

fp=open("emp.csv",'w',newline="")
cw_obj=csv.writer(fp)

cw_obj.writerow(["eid","ename","esal"])
data=[(101,"Rahul",45000),(102,"Sonai",55000),(103,"Priya",65000)]
cw_obj.writerows(data)
print("New CSV File Created")
fp.close()