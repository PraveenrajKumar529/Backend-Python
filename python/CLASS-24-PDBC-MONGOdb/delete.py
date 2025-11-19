from pymongo import MongoClient
client=None
try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['db4']
    user_col=db['users']
    no_users=user_col.count_documents({"gender":"Female"})
    print("No of Users",no_users)
except:
    print('Unable to Perform')
finally:
    pass