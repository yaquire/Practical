#For (a)
tableOfScores =[['Name|','Math','English','Science'],
                ['Benny',89,45,55],
                ['Robin',56,86,23],
                ['Sally',88,81,73],
                ['Aaron',35,75,39],
                ['Simon',65,62,77],]
#For b
print('For (b)')
print('-'*50)
sallyMath = tableOfScores[3][1]
sallyName = tableOfScores[3][0]
print(sallyName,'has scored:', sallyMath)
print('-'*50)
#For c
print('For (c)')
j = 0

for row in tableOfScores:
    
    for i in range(4):
        if i==0:
            print(tableOfScores[j][i]," ",tableOfScores[j][i+1])
    j+=1

i=0
j=0

print('-'*50)
#For D

print('For (d)')
for row in tableOfScores: #one row at a time
    sum = 0
    for col in row: #for this row, iterate column marks
        typeing = isinstance(col,int)
        #print(typeing)
        if typeing == True:
            sum = sum + col
            
        avg = round(sum/3,2)
        print(col," ",end="")
    print(avg,'Average')
    print()
