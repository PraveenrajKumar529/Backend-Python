def outer():
    def f1():
        print("inner function")
    def f2():
        print("inner function")
    def f3():
        print("inner function")
    return 100,200,300
result = outer()
print (result)
print (result[0])
print (result[1])
print (result[2])
