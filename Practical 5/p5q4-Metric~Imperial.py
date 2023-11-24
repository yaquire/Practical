def userInput():
    imperial = input('Input the Fahrenheit: ')

    while True:
        if imperial.isdigit():
            break
        else:
            imperial = input('Please Enter the an INTEGER: ')
    return imperial

def calculator(imperial):
    imperial = int(imperial)
    metric = 5/9*(imperial-32)
    return metric

imperial = userInput()
metric = calculator(imperial)
print('The temperatuer is:',metric)