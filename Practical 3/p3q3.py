score  = input('Please Enter Number: ')

while not type(score) is int: 
    try:
        score = int(score)

        if score >100 or score <0:
            print('Error')
            score  =  input('Please enter a number between 0 and 100: ')
    except ValueError:
        score = input("Please Enter a NUMBER: ")
    
if score >79:
    grade = 'A'
elif score >74:
    grade = 'B+'
elif score >69:
    grade = 'B'
elif score >64:
    grade = 'C+'
elif score >59:
    grade = 'C'
elif score >54:
    grade = 'D'
elif score >49:
    grade = 'E'
else:
    grade = 'F'

print('Your grade is:',grade)
print('Your score is:',score)