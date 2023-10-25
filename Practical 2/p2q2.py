border = '-'
print(border*50)

mass = float(input('Please Enter your mass/weight in (kg): '))
height = float(input('Please Enter your height in (m): '))

bodyMassIndex = round(mass/(height*height),1)


print(border*50)

if bodyMassIndex<18.5:
    weightStatus = 'Underweight'
elif bodyMassIndex>=18.5 and bodyMassIndex<=24.9:
    weightStatus = 'Normal'
elif bodyMassIndex>=25 and bodyMassIndex<=29.9:
    weightStatus = 'Overweight'
else:
    weightStatus = 'Obese'

print('Your status is:',weightStatus)
print('Your BMI is:', bodyMassIndex)

print(border*50)
