border = '-'
print(border*50)

score = int(input('Please enter your score: '))

print(border*50)

if score>= 80:
    grade = 'A'
elif score<80 and score>=70:
    grade = 'B'
elif score<70 and score>=60:
    grade = 'C'
elif score<60 and score>=50:
    grade = 'D'
else: 
    grade = 'F'

print('Your Grade is:',grade)
print(border*50)