border = '='
print(border*50)
print('\t BUBBLE TIAM')
print(border*50)
print('1. Coffee')
print('2. Tea')
print('3. Bubble Tea')
print('0. No Thanks')

border = '-'
print(border*50)

choice = input('Enter 1,2,3 or 0 to exit : ')
print(border*50)


while not choice == '1' and not choice == '2' and not choice == '3' and not choice == '0':
    choice = input('ENTER integer 1,2,3 or 0 only: ')
    print(border*50)

if choice == '1':
    print('You chose Coffee.')
    print(border*50)


elif choice == '2':
    print('You chose Tea')
    print(border*50)


elif choice == '3':
    print('You choose Bubble tea.')
    print(border*50)


else:
    print('Thank you! Bye bye!')
