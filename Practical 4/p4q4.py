#For (a)
tableOfScores =[['Name|','Math','English','Science'],
                ['Benny',89,45,55],
                ['Robin',56,86,23],
                ['Sally',88,81,73],
                ['Aaron',35,75,39],
                ['Simon',65,62,77],]

#For (b)
print('-'*50)
sallyMath = tableOfScores[3][1]
sallyName = tableOfScores[3][0]
print(sallyName,'has scored:', sallyMath)
print('-'*50)

#For (c)
j = 0
for row in tableOfScores:
    
    for i in range(4):
        if i==0:
            print(tableOfScores[j][i]," ",tableOfScores[j][i+1])
    j+=1

print('-'*50)
#For (d)
for i in range(6): #one row at a time
    for col in tableOfScores[i]: #for this row, iterate column tableOfScores
        j=1
        while j<3:
            sum =int(tableOfScores[i+1][j])
            
        
        print(col,"  ",sum,end="|")
    print()

