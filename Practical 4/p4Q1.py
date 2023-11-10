numberList = []
#a = []
i=0

numberOne = int(input('Please enter the 1st No: '))
numberTwo = int(input('Please enter the 2nd No: '))

while i <=50: 
    #a = []
    #a.append(i)

    if i%2==0 or i==0:
        numberList.append(numberTwo)
    else: 
        numberList.append(numberOne)
    
    i+=1

#print(a)
print(numberList)