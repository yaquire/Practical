#a
def getInput():
    rank  = int(input('What is your Rank? '))

    if rank >5:
        print('Your rank is: Others')

    elif rank == 4:
        print('Your rank is: 4th')

    elif rank==3:
        print('Your rank is: 3rd')

    elif rank==2:
        print('Your rank is: 2nd')

    elif rank ==1:
        print('Your rank is: 1st')

    else: 
        print('You have exited the program!')

