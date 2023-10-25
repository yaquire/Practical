border = '-'
print(border*50)

year = int(input('Please Enter the Year: '))
print(border*50)

remainder = 0

if ((year%4 ==remainder)and(year%100 != remainder)) or (year%400 == remainder):
    decision = 'a Leap Year'

else: 
    decision = 'NOT a Leap Year'

print(year,'is',decision)
print(border*50)