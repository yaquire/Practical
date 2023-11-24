def getInput(number):
    numero = input('Please Enter the '+number+' integer: ')
    
    while True:
        if numero.isdigit():
            break
        else:
            numero = input('Please Enter the an INTEGER: ')
    return numero

def findMax(num1,num2):

    num1 = int(num1)
    num2 = int(num2)
    print(type(num1))
    print(type(num2))
    if num1>num2:
        results = "1st number is bigger"

    elif num1<num2:
        results = "2nd number is bigger"

    elif num1 == num2:
        results = "The 2 numbers are equal"
    else:
        results = "ERROR"

    return results



numeroUno =   getInput('1st')        
numeroDos = getInput('2nd')

print(findMax(numeroUno,numeroDos))


#ISSUE WITH def findMAX()