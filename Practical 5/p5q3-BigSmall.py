def getInput():
    numeroUno = input('Please Enter the 1st integer: ')
    numeroDos = input('Please Enter the 2nd integer: ')

    while True:
        try:
            numeroUno = int(numeroUno)
        except ValueError:
            numeroUno = input('Please Enter the 1st INTEGER: ')

    while True:
        try:
            numeroDos = int(numeroDos)
        except ValueError:
            numeroDos = input('Please Enter the 2st INTEGER: ')


