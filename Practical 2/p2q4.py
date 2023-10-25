border = '-'
print(border*50)

employmentLength = int(input('Please Enter the No. of years you have worked here: '))
salary = int(input('Please Enter your salary: '))

print(border*50)

if employmentLength<10:
    if salary<1000:
        increment = 100
    elif salary>=1000 and salary<2000:
        increment = 200
    else: 
        increment = 300
else:
    if salary<1000:
        increment = 100
    elif salary>=1000 and salary<2000:
        increment = 200
    else: 
        increment = 300

rate = increment/salary*100
print('Your rate of increment is:', rate)
increment = str(increment)
print('Your increment is: $'+increment)
print(border*50)
