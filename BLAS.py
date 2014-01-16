# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:35:36 2013

@author: Christian Charukiewicz (netid: charuki1)

This program serves to demonstrate the differences between different BLAS operations. Creates random vectors and matrices, then measures the time for operations to execute. 

Level One: vector-vector operations
Level Two: matrix-vector operations
Level Three: matrix-matrix operations

More info: http://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms

"""

import numpy
import time
import matplotlib.pyplot as plt


vec1 = []
vec2 = []
mat1 = []
mat2 = []

timel1 = []
timel2 = []
timel3 = []

nval1 = []
nval2 = []
nval3 = []

multiplier = 5

def initValues(n):
    global vec1
    global vec2
    global mat1
    global mat2
    vec1 = numpy.random.rand(n)
    vec2 = numpy.random.rand(n)
    mat1 = numpy.random.rand(n,n)
    mat2 = numpy.random.rand(n,n)
    return

def levelOne():
    print "***** LEVEL ONE *****"    
    for n in range(1,11):
        nval = multiplier*n
        initValues(nval)
        t0 = time.time()
        numpy.dot(vec1,vec2)
        endtime = time.time() - t0
        print "n VALUE:", nval, "TIME:", endtime
        timel1.append(endtime)
        nval1.append(nval)
        
def levelTwo():
    print "***** LEVEL TWO *****"    
    for n in range(1,11):
        nval = multiplier*n
        initValues(nval)
        t0 = time.time()
        numpy.dot(vec1,mat1)
        endtime = time.time() - t0
        print "n VALUE:", nval, "TIME:", endtime
        timel2.append(endtime)
        nval2.append(nval)
        
def levelThree():
    print "***** LEVEL THREE *****"    
    for n in range(1,11):
        nval = multiplier*n
        initValues(nval)
        t0 = time.time()
        numpy.dot(mat1,mat2)
        endtime = time.time() - t0
        print "n VALUE:", nval, "TIME:", endtime
        timel3.append(endtime)
        nval3.append(nval)
        
levelOne()
levelTwo()
levelThree()

xmax = max(nval1)
ymax = max(timel3)

xmax = xmax*1.1
ymax = ymax*1.1


print xmax
print ymax

plt.axis([0, xmax, 0, ymax])
plt.plot(nval1, timel1, 'ro', nval2, timel2, 'bs', nval3, timel3, 'g^')
plt.show()
