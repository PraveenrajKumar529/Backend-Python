emp = {
    "eid":101,
    "ename":"rahul",
    "esal":45000
}
print(emp.get("eid"))
print(emp.get("loc"))

for key in emp.keys():
    print(key,":",emp.get(key))