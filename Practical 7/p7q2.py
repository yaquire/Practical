userInput = input('Please Enter your string:')


common = {}

for item in userInput:
    count = 1
    if item not in common:
        common[item]=1
        count =0

    if count !=0:
        common[item]=1+common[item]

for item in sorted(common):
    print(common[item],item)