#Extract - from Rest API
import requests,json,pymongo,csv,mysql.connector
product_resp=requests.get('https://dummyjson.com/products')
product_data=product_resp.json()

products=product_data['products']
print(len(products))


#Transfor - based on requirement
product_json=[]
for product in products:
    product_json.append({"pid":product['id'],
                         "name":product['title'],
                         "price":product['price'],
                         "category":product['category'],
                         "rating":product['rating']
                         })

#print(product_json)
#Load     - into JSON,MongoDB,CSV,Mysql Table
#JSON and MongoDB -Collection
fp2=open("products.json",'w')
json.dump(product_json,fp2)
print("New JSON File created")

