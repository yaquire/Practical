#while Loop
num1 = (input("number1: "))
while not type(num1) is  int: 
    try: 
        num1 = int(num1)
    except ValueError:
        num1 = input('Number1: ')


num2 = (input("number2: "))
while not type(num2) is  int: 
    try: 
        num2 = int(num2)
    except ValueError:
        num2 = input('Number2: ')


num3 = (input("number3: "))
while not type(num3) is  int: 
    try: 
        num3 = int(num3)
    except ValueError:
        num3 = input('Number3: ')


num4 = input('Number4: ')
while not type(num4) is int:
    try: 
        num4 = int(num4)
    except ValueError:
        num4 = input('Number4: ')


num5 = input('Number5: ')
while not type(num5) is int:
    try: 
        num5 = int(num5)
    except ValueError:
        num5 = input('Number5: ')

sumOFNumbers = num5 +num1 +num2 + num3 +num4

print('Sum of Numbers:',sumOFNumbers)