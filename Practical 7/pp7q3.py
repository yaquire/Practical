dict={}
list=[]
def populateDictonary(filename):
    with open(filename) as file:
        data=file.readlines()
        
    for item in data:
        x = item.split(' ')
        list.append(x)
    print(list)

def translateWord(word):
    print()
def removeWord(word):
    print()






#main code
#prompt user for file name of translations
filename = input('Please Enter the file name:')
#call populateDictionary to populate the dict
populateDictonary(filename)

while True:
    print('t-translate word\nr-remove word\nq-quit')
    choice = input('Please enter your choice:')
    choice = choice.upper()
    if choice=='Q':
        break
    else:
        if choice =='P':
            word = input('Please enter the word to be translated:')
            translateWord(word)
        elif choice == 'R':
            word = input('Please enter the word to be translated:')
            removeWord(word)
        else:
            print('Input Invalid\ntry again')