border = '-'
print(50*border)

print(' Sum and Divisibility Check Calculator')
print(50*border)

num1 = int(input('Enter the 1st integer: '))
num2 = int(input('Enter the 2nd integer: '))

total = num1+num2
correct = 0
remainder = num1%num2

divisible = bool(remainder == correct)
print(50*border)

print('The SUM of ',num1,' + ',num2,' = ',total)
print(num1,'is divisible by ',num2,' ? (True or False) : ',divisible)
print(50*border)
