#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 18:15:18 2021

@author: brianroepke
"""
user_input = 0
ok = False

while not ok:
    user_input = input("What is your Age? ")
    try:
        val = int(user_input)
        ok = True

    except ValueError:
        print("Invalid type. Please try again ")
