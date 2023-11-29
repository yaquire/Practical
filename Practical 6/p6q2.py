fileName = input('Please Enter the input file name:')

file = open(fileName,'r')
data = file.readlines()
#print(data)

sum =0
for i in range(len(data)):
    sum += int(data[i])
totalNumbers = len(data)
average = round((sum/totalNumbers),2)
print(fileName+' contains',totalNumbers,'numbers')
print('The total sum of all the',totalNumbers,'is',sum)
print('The average of the numbers is:',average)
