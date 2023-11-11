 
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

for i in range(len(basket)):
    current = basket(i)
    if current is type(str):
        basketFruits.append(current)
    
print(basketFruits)