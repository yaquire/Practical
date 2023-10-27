border = '-'
print(border*50)

format = input('Please Enter if you want to use imperial(I) or Metric(M): ')

if format == 'I' or format == 'i':
    massI = float(input('Please Enter your mass/weight in (lbs): '))
    heightI = float(input('Please Enter your height in (inchs): '))
    bodyMassIndex = round((703*massI/(heightI*heightI)),1)

else:
    massM = float(input('Please Enter your mass/weight in (kg): '))
    heightM = float(input('Please Enter your height in (m): '))
    bodyMassIndex = round((massM/(heightM*heightM)),1)


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
