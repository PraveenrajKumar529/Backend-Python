#read data.txt file and 
# write data into new file i.e wish.txt file
fp=open('wish.txt','w')
data='''Hello rahul GM'''
fp.write(data)
print("New File created")

fp.close()