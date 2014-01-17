# -*- coding: utf-8 -*-
"""
@author: Christian Charukiewicz (netid: charuki1)

This program uses the Monte Carlo method to approximate the given function (defined as f(x) below).

More info: http://en.wikipedia.org/wiki/Monte_Carlo_method

"""

import math
import random

def f(x):
    return (1-x**2)**0.5
    
xmin = 0.0
xmax = 1.0
ymin = f(xmin)
ymax = ymin

n = 1000001

for i in range(n):
    x = xmin + (xmax - xmin) * float(i)/n
    y = f(x)
    if y < ymin: ymin = y
    if y > ymax: ymax = y

area = (xmax - xmin)*(ymax - ymin)
counter = 0
for i in range(n):
    x = xmin + (xmax - xmin)*random.random()
    y = ymin + (ymax - ymin)*random.random()
    if f(x) > 0 and y > 0 and y <= f(x):
        counter = counter + 1
    if f(x) < 0 and y < 0 and y >= f(x):
        counter = counter - 1

totalArea = area*(float(counter)/float(n))
print "Area", 4*totalArea