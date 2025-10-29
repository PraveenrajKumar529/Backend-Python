employees=[{"eid":1,"ename":"Augie","gender":"Male"},
{"eid":2,"ename":"Regan","gender":"Male"},
{"eid":3,"ename":"Edwin","gender":"Male"},
{"eid":4,"ename":"Rodger","gender":"Male"},
{"eid":5,"ename":"Isabella","gender":"Female"},
{"eid":6,"ename":"Daphne","gender":"Female"},
{"eid":7,"ename":"Gaylord","gender":"Male"},
{"eid":8,"ename":"Mortie","gender":"Non-binary"},
{"eid":9,"ename":"Mae","gender":"Female"},
{"eid":10,"ename":"Abby","gender":"Female"},
{"eid":11,"ename":"Reider","gender":"Male"},
{"eid":12,"ename":"Adelina","gender":"Female"},
{"eid":13,"ename":"Rozella","gender":"Female"},
{"eid":14,"ename":"Juana","gender":"Female"},
{"eid":15,"ename":"Rufus","gender":"Male"},
{"eid":16,"ename":"Lynnet","gender":"Female"},
{"eid":17,"ename":"Celia","gender":"Female"},
{"eid":18,"ename":"Reta","gender":"Female"},
{"eid":19,"ename":"Glenine","gender":"Female"},
{"eid":20,"ename":"Ingemar","gender":"Male"},
{"eid":21,"ename":"Leupold","gender":"Male"},
{"eid":22,"ename":"Petronille","gender":"Female"},
{"eid":23,"ename":"Zacharia","gender":"Genderfluid"},
{"eid":24,"ename":"Maggie","gender":"Non-binary"},
{"eid":25,"ename":"Rosco","gender":"Male"},
{"eid":26,"ename":"Bernardo","gender":"Male"},
{"eid":27,"ename":"Brian","gender":"Male"},
{"eid":28,"ename":"Clarabelle","gender":"Female"},
{"eid":29,"ename":"Judy","gender":"Female"},
{"eid":30,"ename":"Gardie","gender":"Male"},
{"eid":31,"ename":"Merissa","gender":"Female"},
{"eid":32,"ename":"Gonzales","gender":"Male"},
{"eid":33,"ename":"Vita","gender":"Female"},
{"eid":34,"ename":"Cherrita","gender":"Female"},
{"eid":35,"ename":"Buddie","gender":"Male"},
{"eid":36,"ename":"Katherina","gender":"Female"},
{"eid":37,"ename":"Charleen","gender":"Female"},
{"eid":38,"ename":"Pet","gender":"Female"},
{"eid":39,"ename":"Abby","gender":"Non-binary"},
{"eid":40,"ename":"Mike","gender":"Male"},
{"eid":41,"ename":"Annette","gender":"Female"},
{"eid":42,"ename":"Ewan","gender":"Agender"},
{"eid":43,"ename":"Steve","gender":"Male"},
{"eid":44,"ename":"Sawyere","gender":"Male"},
{"eid":45,"ename":"Rourke","gender":"Male"},
{"eid":46,"ename":"Abbie","gender":"Male"},
{"eid":47,"ename":"Willette","gender":"Female"},
{"eid":48,"ename":"Jennette","gender":"Female"},
{"eid":49,"ename":"Winston","gender":"Male"},
{"eid":50,"ename":"Weber","gender":"Male"},
{"eid":51,"ename":"Rob","gender":"Male"},
{"eid":52,"ename":"Claudianus","gender":"Male"},
{"eid":53,"ename":"Charity","gender":"Female"},
{"eid":54,"ename":"Timmie","gender":"Female"},
{"eid":55,"ename":"Ranique","gender":"Genderqueer"},
{"eid":56,"ename":"Hasty","gender":"Male"},
{"eid":57,"ename":"Gabey","gender":"Female"},
{"eid":58,"ename":"Berton","gender":"Male"},
{"eid":59,"ename":"Cortie","gender":"Male"},
{"eid":60,"ename":"Benn","gender":"Male"},
{"eid":61,"ename":"Jarrid","gender":"Male"},
{"eid":62,"ename":"Eleanora","gender":"Female"},
{"eid":63,"ename":"Zabrina","gender":"Female"},
{"eid":64,"ename":"Foss","gender":"Male"},
{"eid":65,"ename":"Jake","gender":"Male"},
{"eid":66,"ename":"Onida","gender":"Female"},
{"eid":67,"ename":"Matthiew","gender":"Male"},
{"eid":68,"ename":"Chen","gender":"Male"},
{"eid":69,"ename":"Johannah","gender":"Female"},
{"eid":70,"ename":"Merissa","gender":"Female"},
{"eid":71,"ename":"Jone","gender":"Male"},
{"eid":72,"ename":"Meggie","gender":"Female"},
{"eid":73,"ename":"Aldo","gender":"Male"},
{"eid":74,"ename":"Cristin","gender":"Female"},
{"eid":75,"ename":"Opal","gender":"Female"},
{"eid":76,"ename":"Alana","gender":"Non-binary"},
{"eid":77,"ename":"Daveta","gender":"Female"},
{"eid":78,"ename":"Julia","gender":"Female"},
{"eid":79,"ename":"Virge","gender":"Male"},
{"eid":80,"ename":"Reeva","gender":"Female"},
{"eid":81,"ename":"Alexandre","gender":"Male"},
{"eid":82,"ename":"Zenia","gender":"Female"},
{"eid":83,"ename":"Darcee","gender":"Female"},
{"eid":84,"ename":"Bessy","gender":"Female"},
{"eid":85,"ename":"Even","gender":"Male"},
{"eid":86,"ename":"Mignon","gender":"Female"},
{"eid":87,"ename":"Dougie","gender":"Male"},
{"eid":88,"ename":"Chiquia","gender":"Female"},
{"eid":89,"ename":"Gerri","gender":"Female"},
{"eid":90,"ename":"Selby","gender":"Male"},
{"eid":91,"ename":"Zola","gender":"Genderqueer"},
{"eid":92,"ename":"Markos","gender":"Male"},
{"eid":93,"ename":"Steffie","gender":"Female"},
{"eid":94,"ename":"Ellswerth","gender":"Male"},
{"eid":95,"ename":"Erl","gender":"Male"},
{"eid":96,"ename":"Porty","gender":"Male"},
{"eid":97,"ename":"Erhart","gender":"Genderfluid"},
{"eid":98,"ename":"Connie","gender":"Polygender"},
{"eid":99,"ename":"Melvyn","gender":"Male"},
{"eid":100,"ename":"Florinda","gender":"Female"}]

#print all employee name
#using for and while loop
""" for emp in employees:
    print(emp['ename']) """
    
""" i=0
while i<=len(employees)-1:
    print (employees[i] ['ename'])
    i=i+1 """
#key error
""" for employees in employees:
    print(employees['eid'])    
    print(employees['gender'])    
    print(employees['ename'])    
    print(employees['email']) """   #key error
     
#print male and female names using for and while loop
male_count=0
female_count=0
Polygender_count=0
for emp in employees:
    if emp["gender"]=="Male":
        male_count=male_count+1
    elif emp["gender"]=="Female":
        female_count=female_count+1
    else:
        Polygender_count+=1
print("No of male employees:",male_count)
print("No of female employees:",female_count)
print("No of Polygender employees:",Polygender_count)