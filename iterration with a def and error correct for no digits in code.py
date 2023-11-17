def printMsg (msg,times):
        for x in range(0,times):
            print(msg,x+1)


while True:
    msg = input('What statement to iterate? ("e" to exit!)')
    if msg == 'e':
            print('Program Ends \n Thank you have a great day')
            break

    else:
    
        if msg.isdigit():
            print('Error! Only Strings')

               
               
               
        else:
            times = int(input("How many times to iterate?: "))
            printMsg(msg,times)


