def isLeapYear(year):

    if ((year%4==0) and (year%100 !=0))or(year%400==0):
        leapYear = 'IS'
    else:
        leapYear = 'IS NOT'

    return leapYear

def readYear():
    year = int(input('What year is it:'))
    return year

year = readYear()
hasLeapYear = isLeapYear(year)
print(year, hasLeapYear,'leap year')