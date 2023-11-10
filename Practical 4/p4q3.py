mylist = [1,5,6,7,9,100,23,6,5,1]
border = '-'
i = 0

while True:
    instances= mylist.count(mylist[i])
    
    if instances>1:
        mylist.pop(i)
    else:
        mylist.sort()
        print('The new list is: ', mylist)
        break
        

