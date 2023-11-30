fileMovies = 'movies.txt'
fileFruits = 'fruits.txt'

#for MOVIES
file = open(fileMovies,'r')
data = file.readlines()

#this joins the items to make it easier to get rid of the '\n' so that it can be split into multiple items neatly
movies = ''.join(data)
movies = str(movies)
movies = movies.split('\n')

print('For movies:',movies)
file.close()


#for FRUITS
file = open(fileFruits, 'r')
data = file.readlines()

#this joins the items to make it easier to get rid of the '\n' so that it can be split into multiple items neatly
fruits = ''.join(data)
fruits = str(fruits)
fruits = fruits.split('\n')

print('For fruits:',fruits)
file.close