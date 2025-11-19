#delete all male users from collection-users
from pymongo import MongoClient
client=None
try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['db4']
    user_col=db['users']
    user_col.delete_many({"gender":"Male"})
    print("all Male users deleted successfully")
except:
    print("Unable to Peform")
finally:
    pass