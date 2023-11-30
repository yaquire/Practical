#opening FILE
fileName = 'marks.csv'
file = open(fileName,'r')
data = file.readlines()
print(len(data))
totalA = 0
namesA = []
for i in range(1,len(data)):
   
    line = data[i]
    cols = line.split(",")
    name = cols[0]
    mark = int(cols[i])
    if mark >= 80:
        namesA +=1
        namesA.append(name)
print(totalA)
print(namesA)
file.close
#mergeing items to serperate them easier




print(merge)