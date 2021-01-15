#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:16:18 2021

@author: brianroepke
"""

def getTitle():
    genre = input('Enter genre : ')   	        # get user input and assign to genre
    keys = ['title', 'year', 'rating']   		# list of keys
    values = []                       		    # empty list of values
    title = input('Enter movie title: ') 	    # get user input and assign to title
    values.append(title)                    	# append to values list
    year = int(input('Enter movie year: '))    # get user input and assign to year, converted to int
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