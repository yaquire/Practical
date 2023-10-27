border = "-"
print(border * 50)

number1 = int(input("Please enter the 1st between 1-10: "))
number2 = int(input("Please enter the 2nd between 1-10: "))

print(border * 50)

averageNumber = (number1 + number2) / 2

if number1 != number2:
    if number1 > number2:
        largerNumber = number1
        smallerNumber = number2
    elif number2 > number1:
        largerNumber = number2
        smallerNumber = number1

    print("A<B<C")
    print(smallerNumber, "<", averageNumber, "<", largerNumber)
else:
    print("A=B=C")
    print(number1, "=", number1, "=", number1)


print(border * 50)
