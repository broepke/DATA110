#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:16:18 2021

@author: brianroepke
"""


def getTitle():
    moviesDict = {"movies": {}}
    genre = input('Enter genre : ')
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

    return moviesDict


my_movie = getTitle()
print(my_movie)
