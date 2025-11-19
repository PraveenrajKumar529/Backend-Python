import requests,csv,pymongo,json,mysql.connector
products_resp=requests.get("https://dummyjson.com/products'")
products_data=products_resp.json()
products=products_data["products"]
print(len(products))