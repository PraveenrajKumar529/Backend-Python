#read data.txt file and 
# write data into new file i.e wish.txt file

fp1=open('data.txt','r')
fp2=open('wish.txt','w')
data=fp1.read()
fp2.write(data)
print("New File Created")

fp1.close()
fp2.close()