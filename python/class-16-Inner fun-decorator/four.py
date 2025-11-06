#How to invoke inner funciton from outside
def outer():
    print("outer function")
    
    def inner():
        print("inner function")
        
    """ return 100 """
    return inner
        
inn=outer()
print(inn)
print(type(inn))
inn()
""" inner() #name error """
