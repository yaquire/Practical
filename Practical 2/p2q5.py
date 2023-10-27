border = "-"
print(border * 50)

seaterType = input("Please enter if you used a single or double bike (S/D): ")
duration = int(input("Please enter the number of hours rented: "))

print(border * 50)

if seaterType == "s" or seaterType == "S":
    rate = 5.5
else:
    rate = 7.8


if duration >= 3:
    discountRate = 0.3
else:
    discountRate = 0

rentalFee = rate * duration * (1 - discountRate)

print("Your total cost will be:", round(rentalFee, 2))
print(border * 50)
