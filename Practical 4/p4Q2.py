#assuming no error correction 
list1 = []
border = '-'

while True:
    enteredValue = input('Please enter the numbers or (N) to end: ')

    print(border*50)
    if enteredValue == 'N':
        print('You have Chosen to EXIT!')
        break
    else: 
        enteredValue = int(enteredValue)
        list1.append(enteredValue)

LargestNumber = 0
for i in range(len(list1)):
    if list1[i]>LargestNumber:
        LargestNumber = list1[i]
print(border*50)
print('Your list is: ',list1)
print(border*50)
print('Its seems that ',LargestNumber, 'is the largest number!')