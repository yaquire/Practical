d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d3 = {}
for key1 in d1:
    for key2 in d2:
        if key1 == key2:
            common = d1[key1] +d2[key2]
            print(common)
            d3[key1] = common

        else:
            common = d1[key1] 
            d3[key1] = common

            common = d2[key2]
            d3[key2] = common

print(d3)