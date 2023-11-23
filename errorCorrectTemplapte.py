userInput = input(' Enter a letter : ')
try:
    userInput = int( userInput )
except ValueError:
    print(' Only integer allowed')