from random import choice
coin=["head","tail"]
head_count=0
for i in range(100):
    result=choice(coin)
    if result== "head":
        head_count=head_count+1
print("no of times head",head_count)
print("no of times tail",100-head_count)