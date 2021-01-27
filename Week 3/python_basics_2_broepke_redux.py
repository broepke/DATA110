#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:49:43 2021

@author: brianroepke
"""


def getTitle():
    keys = ['title', 'year', 'rating']
    values = []

    title = input('Enter movie title: ')
    values.append(title)
    year = int(input('Enter movie year: '))
    values.append(year)
    rating = float(input("Enter movie rating: "))
    values.append(rating)

    d = {k: v for k, v in zip(keys, values)}

    return d


moviesDict = {"movies": {}}
genre = input('Enter genre name: ')


titles = []
# Request the user enter 5 movie titles
for i in range(5):
    user_title = getTitle()
    titles.append(user_title)


moviesDict['movies'][genre] = titles

genres = moviesDict['movies']
for gen in genres:
    print(gen)
    total = 0
    count = 0
    for movies in genres[gen]:
        print(
            f"movie: {movies['title']}, year: "
            f"{movies['year']}, rating: {movies['rating']}")
        total += movies['rating']
        count += 1
    print(f"{gen} avg movie rating: {total/count}")
    print('')
