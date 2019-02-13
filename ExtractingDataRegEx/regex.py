#!/usr/bin/env python3

# Zachery Smith ~  zrs3141592@gmail.com
# Coursera Using Python to Access Web Data
# Week 1: Extracting Data with Regular Expressions

import re
x = 'My 2 favorite numbers are 19 and 23'
y = re.findall('[0-9]', x)
print(y)
