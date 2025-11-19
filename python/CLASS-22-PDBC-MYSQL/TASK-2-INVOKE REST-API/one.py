import requests
import json
import csv
import mysql.connector # Kept, but not used in this script's functionality

# Open files for writing
fp1 = open("user.json", "w")
fp2 = open('user.csv', 'w', newline="")

# Fetch data
user_resp = requests.get('https://dummyjson.com/products')
all_data = user_resp.json()

# CRITICAL FIX 1: Access the list of products using the 'products' key
products = all_data.get('products', []) 

# Initialize lists for transformed data
user_csv_data = []
user_json_data = []

# Transform for CSV File and JSON file
for product in products:
    # CRITICAL FIX 2: Use the correct API field names: 'title', 'price', 'description'
    product_id = product.get('id')
    product_title = product.get('title')
    product_price = product.get('price')
    product_details = product.get('description') 

    # Append data for CSV (as a tuple)
    user_csv_data.append((
        product_id,
        product_title,
        product_price,
        product_details
    ))
    
    # Append data for JSON (as a dictionary)
    user_json_data.append({
        "id": product_id,
        "pname": product_title,      # Renamed for your desired output structure
        "p_price": product_price,    # Renamed for your desired output structure
        "pdetails": product_details  # Renamed for your desired output structure
    })

# Write data to JSON file
json.dump(user_json_data, fp1, indent=4) # Added indent for readability
fp1.close() # Close file handle
print("New JSON File is Created (user.json)")

# Write data to CSV file
cw_obj = csv.writer(fp2)
cw_obj.writerow(["id", "pname", "p_price", "pdetails"]) # Write header
cw_obj.writerows(user_csv_data)
fp2.close() # Close file handle
print("New CSV File Created Successfully (user.csv)")

import mysql.connector
dbcon=None 
cursor=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='db5') 
    cursor=dbcon.cursor()
    sql_st='''
            create table users(
            pid int,
            pname varchar(32),
            p_price varchar(32),
            pdetails varchar(32)
            );
            '''
    sql_st1='''
            insert into users(pid,pname,p_price,pdetails) values(%s,%s,%s,%s)
            '''
    cursor.execute(sql_st)
    cursor.executemany(sql_st1,user_csv_data)
    dbcon.commit()
    print("SQL TABLE CREATED Successfully!")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()