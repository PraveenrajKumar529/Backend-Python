import pymongo
from pymongo import MongoClient
client=None
try:
    client=MongoClient("mongodb://localhost:27017/")
    db=client["db4"]
    user_col=db["users"]
    
    pass

except:
    pass

finally:
    pass