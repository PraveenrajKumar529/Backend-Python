from fastapi import FastAPI
#create fastapi app
app=FastAPI()

@app.get("/")
def index_page():
    return {"message":"Index Page"}
'''
usage:About Request
Rest API URL:http:127.0.0.1:8000/about
Method Type:GET
Required Fields:None
Access Type:Public
'''
@app.get('/about')
def about_page():
    return {"message":"About Request"}
from fastapi import FastAPI
#create fastapi app
app=FastAPI()

'''
usage:Application Root Request
Rest API URL:http:127.0.0.1:8000/
Method Type:GET
Required Fields:None
Access Type:Public
'''
@app.get("/")
def index_page():
    return {"message":"Index Page"}

'''
usage:About Request
Rest API URL:http:127.0.0.1:8000/about
Method Type:GET
Required Fields:None
Access Type:Public
'''
@app.get('/about')
def about_page():
    return {"message":"About Request"}


'''
usage:contact Request
Rest API URL:http:127.0.0.1:8000/contact
Method Type:GET
Required Fields:None
Access Type:Public
'''

@app.get("/contact")
def contact_page():
    return {"message":"Contact Page"}