#default arguments-function
def sum(a,b,c=100,d): #always default arg are must be last
    print(a+b+c+d)
    
    sum(1,2,3,4) #6
    sum(1,2,)  #103