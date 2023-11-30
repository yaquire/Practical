fileName = 'marks.csv'
file = open(fileName,'r')
data = file.readlines()
#Method 1
#Merging the lists to remove '\n'
merging = ''.join(data)
merging = str(merging)
merging = merging.split('\n')

outerList = []
for i in range(1,len(merging)):
    
    item = merging[i]
    item = item.split(',')
    outerList.append(item)


print(outerList)
file.close()

#Method 2
with open('marks.csv') as file:
    data = file.readlines()

merging = ''.join(data)
merging = str(merging)
merging = merging.split('\n')

outerList = []
for i in range(1,len(merging)):
    
    item = merging[i]
    item = item.split(',')
    outerList.append(item)


print(outerList)
file.close()