from fastapi import FastAPI

app=FastAPI()
'''
Usage:Application Root Req
Rest API URL:http://127.0.0.1:8000
Method Type:GET
Required Fields:None 
Access Type:Public
'''
@app.get("/")
def index_page():
    return {"message":"Application Root request"}

'''
Create
------
usage:create new user 
Rest API URL: http://127.0.0.1:8000/create 
Method Type:POST
Required Fiels: uid,uname,email
Access Type:Public
'''
@app.post("/create")
def create_User():
    return {"message":"User Created Successfully"}



'''
Read
-----
usage:fetch user details 
Rest API URL: http://127.0.0.1:8000/read 
Method Type:GET 
Required Fiels:None 
Access Type:Public 
'''
@app.get("/read")
def user_details():
    return {"message":"Fetching User Details"}


'''
Update
-----
usage:update user 
Rest API URL: http://127.0.0.1:8000/update 
Method Type:PUT 
Required Fiels:None 
Access Type:Public 
'''
@app.put("/update")
def update_user():
    return {"message":"User Updated Successfully"}


'''
Delete
------
usage:Delete  user 
Rest API URL: http://127.0.0.1:8000/del
Method Type:Delete
Required Fiels: None 
Access Type:Public
'''
@app.delete("/del")
def delete_User():
    return {"message":"User Deleted"}