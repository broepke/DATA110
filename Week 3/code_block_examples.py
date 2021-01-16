#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 18:45:40 2021

@author: brianroepke
"""

# %%

a = 2
b = 5

print(a + b)

# %%


def grade(score):
    # A 90-100
    if score >= 90:
        return 'A'
    elif (score >= 80) and (score <= 89):
        return 'B'
    # B 80-89
    elif (score >= 70) and (score <= 79):
        return 'C'
    # C 70-79
    elif (score >= 60) and (score <= 69):
        return 'D'
    # D 60-69
    else:
        return 'F'


print(grade(81))
print(grade(90))
print(grade(75))
print(grade(69))
print(grade(59))

# %%
