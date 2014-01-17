# -*- coding: utf-8 -*-

"""
@author: Christian Charukiewicz (netid: charuki1)

This program is a simulation of the Monte Carlo method to demonstrate how it works in a more practical application.

Problem text:

"This problem will involve simulating a random walk with a Monte Carlo simulation.
Suppose a drunkard leaves a bar located at a point (0, 0) in a two-dimensional coordinate system.
His home is located at the point (3, 4).
Assume he steps either North, South, East, or West, each with equal probability.
What is the probability that at any point in taking 25 steps he ends up at home?
To determine the probability repeat the walk 30000 times."

We can observe different results by changing the n variable.

"""

import math
import numpy as np
import random

arrived = 0.
n = 30000   # number of walks
A = [0,0]

def drunkwalk():
    for i in range(n):
        for j in range(25):
            temp = random.random()*100
            if(temp<=25):
                A[0] += 1
            if(temp>25 and temp<=50):
                A[0] -= 1
            if(temp>50 and temp<=75):
                A[1] += 1
            if(temp>75):
                A[1] -= 1
            if(A[0]==3 and A[1]==4):
                global arrived
                arrived = arrived + 1
                break
        A[0] = 0
        A[1] = 0

drunkwalk()


print "ARRIVALS:", arrived
print "PROBABILITY:", arrived/n