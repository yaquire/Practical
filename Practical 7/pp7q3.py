def populateDictonary(filename):
    with open(filename) as file:
        data=file.readlines()
        print(data)

#main code
#prompt user for file name of translations
filenama = input('Please Enter the file name:')
#call populateDictionary to populate the dict
populateDictonary(filenama)

