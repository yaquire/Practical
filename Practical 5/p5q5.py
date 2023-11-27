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
    for i in range(n+1):
        print(i*n)


def printPattern2(n):
#part d






#pat = choosePattern()
#num = readInput()

