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




'''''for key1 in d1:
    print('1'+key1)
    for key2 in d2:
        print('2'+key2)
        if key1 == key2:
            common = d1[key1] +d2[key2]
            print(common)
           
            d3[key1] = common
            print(d3)
        else:
            common = d1[key1] 
            d3[key1] = common

            common = d2[key2]
            d3[key2] = common

print('Sample Output: d3 =',d3)'''