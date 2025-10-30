prod_prices=[99,199,299,399,499,599,699,799,899,999]
""" for price in prod_prices:
    if price>500:
        break
    print(price) """

i=0
while i<=len(prod_prices)-1:
    if prod_prices[i]>500:
        break
    print(prod_prices[i])
    i=i+1
    
        
    