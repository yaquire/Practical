border = '-'
print(50*border)
print(' Module Score Calculator')
print(50*border)

MST = int(input('Enter your MST score \t\t\t:'))
assign1 = int(input('Enter your assignment 1 score \t\t:'))
assign2 = int(input('Enter your assignment 2 score \t\t:'))
GP = int(input('Enter your General Performance score \t:'))

finalScore = .2*MST+.25*assign1+.35*assign2+.2*GP

print(50*border)
print('Your module score is ', round(finalScore,1))
print(50*border)