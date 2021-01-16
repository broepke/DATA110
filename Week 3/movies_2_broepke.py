#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. Create a function getTitle that asks for user input for
(title, year, rating) and return a dictionary with the user values.
Make sure to include exception handling of invalid input types.

2. Create a function displayMovies which takes a dictionary as an input
parameter and prints the details of each movie genre, along with all
movies within a genre.

3. Instead of defining a partially populated movie dictionary, you should
start with an empty dictionary which gets added to given calls to getTitle.

4. Also instead of a static 5 genres, use while loop which terminate
based on user input of  "quit" for genre.
There will still be 5 movie titles per genre.
"""


def getTitle():
    done = False
    moviesDict = {"movies": {}}
    while not done:
        genre = input('Enter genre : ')
        if genre.lower() == "quit":
            done = True
            return moviesDict
        else:
            keys = ['title', 'year', 'rating']
            titles = []
            count = 5
            total = 0

            # Request the user enter 5 movie titles
            for i in range(count):
                values = []

                ok = False
                while not ok:
                    title = input('Enter movie title: ')
                    try:
                        val = str(title)
                        ok = True
                        values.append(val)
                    except ValueError:
                        print("Invalid type. Please try again")

                ok = False
                while not ok:
                    year = input('Enter movie year: ')
                    try:
                        val = int(year)
                        ok = True
                        values.append(val)
                    except ValueError:
                        print("Invalid type. Please try again")

                ok = False
                while not ok:
                    rating = input("Enter movie rating: ")
                    try:
                        val = float(rating)
                        ok = True
                        values.append(val)
                    except ValueError:
                        print("Invalid type. Please try again")

                d = {k: v for k, v in zip(keys, values)}
                titles.append(d)

            moviesDict['movies'][genre] = titles


def displayMovies(mov_dict):
    genres = mov_dict['movies']
    for gen in genres:
        print(gen)
        total = 0
        count = 0
        for movies in genres[gen]:
            print("movie: {}, year: {}, rating: {}".format(
                movies['title'], movies['year'], movies['rating']))
            total += movies['rating']
            count += 1
        print('{} avg movie rating: {}'.format(gen, total/count))
        print('')


print("This program will continue until you type the word QUIT for the Genre")

my_movie = getTitle()


try:
    displayMovies(my_movie)
except TypeError:
    print("Thank you!")
