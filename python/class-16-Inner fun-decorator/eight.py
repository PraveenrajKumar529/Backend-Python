def add(a,b):
    def inner():
        print("inner")
    return a+b,"niharika",inner
result=add(10,20)
print(result) #30
result[2]()
result[2]()
result[2]()