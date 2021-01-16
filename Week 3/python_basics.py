#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:16:18 2021

@author: brianroepke
"""


def getTitle():
    # get user input and assign to genre
    genre = input('Enter genre : ')
    # list of keys
    keys = ['title', 'year', 'rating']
    # empty list of values
    values = []
    # get user input and assign to title
    title = input('Enter movie title: ')
    # append to values list
    values.append(title)
    # get user input and assign to year, converted to int
    year = int(input('Enter movie year: '))
    values.append(year)
    rating = float(input("Enter movie rating: "))
    values.append(rating)

    # dictionary comprehension to create a dictionary
    d = {k: v for k, v in zip(keys, values)}
    # dictionary with key: genre, key: list of dictionaries
    d2 = {genre: [d]}
    return d2


my_movie = getTitle()

print(my_movie)