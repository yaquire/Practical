with open('student.txt') as file:

    data = file.read()

    data = data.split('\n')
    print(data)

    outerList = []
    for i in range(1,len(data)):
        item = data[i]
        item = item.split(',')
        outerList.append(item)

    print(outerList)