prod_prices = [999, 99, 199, 399, 299, 499, 799, 899, 599, 699]
""" i = 0
while i <= len(prod_prices) - 1:
    if prod_prices[i] > 500:
        i = i + 1 
        continue   
    print(prod_prices[i])
    i = i + 1 """
    
for price in prod_prices:
    if price>500:
        continue
    print(price)