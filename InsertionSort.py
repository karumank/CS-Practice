#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:19:58 2019

@author: Krishna

TOPIC: Insertion Sort
"""

inputArray = [3,1,5,6,7,2]

for x in range(1, len(inputArray)):
    key = inputArray[x]
    y = x
    while y > 0 and inputArray[y - 1] > key:
        inputArray[y] = inputArray[y - 1]
        y = y - 1
    inputArray[y] = key

print (inputArray)
    
    

