#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 06:13:05 2021

@author: brianroepke
"""

# My Solution
genres = moviesDict['movies']
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


# Provided Solution
genres = moviesDict['movies']
for gen in genres:
    print(gen)
    movies = moviesDict['movies'][gen]

    avgRating = 0
    for m in movies:
        title = m['title']
        year = m['year']
        rating = m['rating']
        avgRating = avgRating + rating
        print(f'movie: {title}, year: {year}, rating: {rating}')

    avgRating = avgRating / len(movies)
    print(f'{gen} avg movie rating: {avgRating}')
    print()
