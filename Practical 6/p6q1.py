#For part a
fileName = ('greeting.txt')

file = open(fileName,'w')
data = file.writelines('Hello Sir!\n')

file.close()

#For part b
file = open(fileName, 'a')
data = file.writelines('How are you?\n')
data = file.writelines('Hope your are fine\n')

file.close()

file = open(fileName,'r')
data = file.readlines()
print(data)
file.close()