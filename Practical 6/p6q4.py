#opening FILE
fileName = 'marks.csv'
file = open(fileName,'r')
data = file.readlines()

totalA = 0
namesA = []
for i in range(1,len(data)):
   
    line = data[i]
    cols = line.split(",")
    name = cols[0]
    mark = int(cols[1])
    if mark >= 80:
        totalA +=1
        namesA.append(name)
print('The number for A are:',totalA)
print('The people who scored A is:',namesA)
file.close