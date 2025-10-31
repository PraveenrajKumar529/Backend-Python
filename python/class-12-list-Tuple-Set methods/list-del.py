eids=[101,102,103,104]
eids.pop() #remove last element from list

print(eids) #[101,102,103]

eids.remove(102) #remove specified element from list
print(eids)      #[101,103]

eids.clear()

print(eids)

del eids
print(eids) #name error