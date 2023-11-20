 
basket = ["Apple", 2,"Orange", 5, "Banana", 10, "Pear", 2 ,5, "Apple",
50, "Banana",2, "Orange",50,10]

#Ans for 1:
sum =0
for num in basket:
    if num==5:
        sum +=1
print('Number of $5 notes:',sum,
      'First instance of $5:',basket.index(5))
print('-'*50)
#Ans for 2: 
bananaNoOne = basket.index('Banana')
basket.insert(bananaNoOne+1,'Durian')
print(basket)
print('-'*50)
#Ans for 3: 
basketNotes = []
basketFruits = []

for item in basket:

    thing  = isinstance(item,int)
    if thing == False:
        basketFruits.append(item) 
    elif thing == True:
        basketNotes.append(item)
    else: 
        print('!')
        
print("Notes:",basketNotes)
print('Fruits:',basketFruits)
#print(basket)

#Ans for 4: 
print('-'*50)
basketFruits.sort()
print('Assending:',basketFruits)

#Ans for 5:
print('-'*50)
basketFruits.sort(reverse=True)
print('Desending:',basketFruits)

#Ans for 6: 
print('-'*50)
sum=0
notes = 0
bigger,smaller = 0,100000000
for item in basketNotes:
    sum = sum + item 
    notes+=1

    if bigger<item:
        bigger=item
    if smaller>item:
        smaller=item
    
print('Total: SGD',sum)
print('Biggest:', bigger)
print('Smallest:', smaller)
print('Total Notes:',notes)

#Ans for 7: 
print('-'*50)
happenedBefore = 0
unique = ''
for item in basketFruits:
    if unique != item:
        happenedBefore +=1
        unique=item

print('UniqueNess:',happenedBefore)

#Ans for 8: 
print('-'*50)

instances = 0
basketNotes.sort()
print(basketNotes)
for item in basketNotes:
    if 2 == item:
        instances+=1
    
for i in range(0,instances):
    	basketNotes.pop(0)

print('Smallest-Biggest:',basketNotes)
