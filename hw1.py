#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 18:26:50 2020

@author: laura
"""

### Home work 1 
# ----------------------------------------------------------- #
## Problem 1:

# (a) [1,2,3,...,19,20]
a = list(range(1,21))
print(a)

# (b) [20,19,...,2,1]
b = a[:]  # or b = a.copy()
b.reverse()
print(b)

# (c) [1,2,3,...,19,20,19,18,...,2,1]
c = a[:]+b[1:21]
print(c)

# For parts (d) and (e) try the syntax “N * [val1,val2]” and the del command.
# (d) [4,6,3, 4,6,3,...,4,6,3] where there are 10 occurrences of 4.
d = [4,6,3]*4
print(d)

#(e) [4,6,3, 4,6,3,...,4,6,3,4] where there are 11 occurrences of 4, 10 occurrences of 6 and 10 occur- rences of 3.
e = [4,6,3]*10+[4]
print(e)

# ----------------------------------------------------------- #
## Problem 2:
import numpy as np

num_list=[x*0.1+3 for x in range(0, 31)]
new_list=[np.exp(x)*np.cos(x) for x in num_list]
print(new_list)

# ----------------------------------------------------------- #
## Problem 3:
list_3 = [2**x/x for x in range(1,26)]
print(list_3)

# ----------------------------------------------------------- #
## Problem 4: Re-use your list from 1(a) as variable a. It has length n. Create these lists:
#(a) [a0 – an, a1 – an-1,...,an-a0]

list_4_a = [a[x]-a[-1-x] for x in range(len(a))]
print(list_4_a)

#(b) A Boolean list where even values of a are True and odd values are False: [False, True,...].

boolean = [(x % 2)==0 for x in a]
print(boolean)


# ----------------------------------------------------------- #
## Problem 5: Write a Python script that will open the file lorem.txt. The script will read the file and compute these quantities:
#(a) The number of strings whose lengths are: between 1 and 4, between 4 and 7, and 8 or greater.
#(b) The number of capitalized characters in the file.

import re

## read file:
with open('lorem.txt','r') as f:
    # Read the contents into a list of strings
    all_lines = f.readlines()
    # This will always close the file but do it
    # anyway...it's a good habit.
    f.close()

#delimiters = ['\n', ' ', ',', '.', '?', '!', ':', ';']
#words = re.split(r'[;,\s,.,:]\s*', all_lines[0])
#print(words)
#words = [re.split(r'[;,\s,.,:]\s*', line) for line in all_lines]

## solution for a:
words = []
for line in all_lines:
    words.extend(re.split(r'[;,\s,.,:]\s*', line))

words_4 =[]
words_7 =[]
words_8 =[]
words_0 =[]
for x in words:
    if len(x)>=1 and len(x)<=4:
        words_4.append(x)
    elif len(x)>4 and len(x)<=7:
        words_7.append(x)
    elif len(x)>=8:
        words_8.append(x)
    else:
        words_0.append(x)

print("The number of strings whose lengths are between 1 and 4 is: %s" % (len(words_4)))
print("The number of strings whose lengths are between 4 and 7 is: %s" % (len(words_7)))
print("The number of strings whose lengths are 8 or greater is: %s" % (len(words_8)))

## solution for b:
match = []
for line in all_lines:
    match.extend(re.findall('([A-Z])',line))

print("The number of capitalized characters in the file is: %s" % len(match))













