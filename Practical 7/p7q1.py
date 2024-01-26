d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d3 = {}
key1 = []
key2 = []

for key in d1:
    key1.append(key)    
for key in d2:
    key2.append(key) 

for i in range(3):
    if key1[i]==key2[i]:
        
        common = d1[key2[i]]+d2[key1[i]]
        d3[key2[i]] = common
    else:
        
        common = d1[key1[i]] 
        d3[key1[i]] = common

        common = d2[key2[i]]
        d3[key2[i]] = common

print('d3 = ',d3)




