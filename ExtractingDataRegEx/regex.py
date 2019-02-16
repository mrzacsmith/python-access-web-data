#!/usr/bin/env python3

# Zachery Smith ~  zrs3141592@gmail.com
# Coursera Using Python to Access Web Data
# Week 1: Extracting Data with Regular Expressions

import re

# fileName = "regex_sum_42.txt" # test data

fileName = "regex_sum_189375.txt"

file = open(fileName)
x = list()
for line in file:
     y = re.findall('[0-9]+', line)
     x = x+y

sum = 0
for z in x:
    sum = sum + int(z)

print(sum)