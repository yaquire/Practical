#NO ERROR CHECKING

border = '-'
print(border*50)

#float cus pH can be in decimal and it isnt specified
levelpH = float(input('Please Enter the pH level measured: '))
print(border*50)

if levelpH>7:
    health = 'alkaline'
elif levelpH <7:
    health = 'acidic'
else:
    health = 'nuetral'

print('The health of the aquarium:',health)
print(border*50)