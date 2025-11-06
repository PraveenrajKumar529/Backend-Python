def calc():
    
    
    def add():
        print("addition")
        
    def multi():
        print("multipilication")
        
    return add,multi

inner=calc()
print(type(inner))
inner[0]()
inner[0]()
inner[1]()
calc()