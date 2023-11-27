def readInput():
#part a
    numberOfRows = input('Please enter the number of row you want:')

    while True:
        if numberOfRows.isdigit():
            break
        else:
            numberOfRows = input('Please Enter the an INTEGER: ')

    return int(numberOfRows)

def choosePattern():
#part b
    print('1) Pattern 1\n2) Pattern 2')
    patternChose = input('Please chose the pattern: ')

    return patternChose
    
def printPattern1(n):
#part c
    print('Pattern 1')

    for i in range(n):
        i = str(i+1)
        print((i+'\t')*n)


def printPattern2(n):
#part d

    print('Pattern 2')
    for i in range(n):
        for j in range(1, n + 1):
            print(j, end='\t')
        print()

pat = choosePattern()
num = readInput()
print(pat)
if pat=='1':
    print(printPattern1(num))
else:
    print(printPattern2(num))