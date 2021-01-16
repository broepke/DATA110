#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:16:18 2021

@author: brianroepke
"""


def getTitle(user_genre):
    moviesDict = {"movies": {}}
    genre = user_genre
    keys = ['title', 'year', 'rating']
    titles = []

    # Request the user enter 5 movie titles
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

    return moviesDict


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


print("#####################################################################")
print("#")
print("This program will continue until you type the word DONE for the Genre")
print("#")
print("#####################################################################")

done = False
while not done:
    genre = input('Enter genre : ')
    if genre.lower() == "done":
        break
    else:
        my_movie = getTitle(genre)

try:
    displayMovies(my_movie)
except NameError:
    print("Thank you!")
