#this has error correction 

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

if num1%2 == 0:
    x = num1+1
else:
    x = num1



for i in range(x,num2,2):
    print(i)