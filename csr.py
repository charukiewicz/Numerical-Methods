# -*- coding: utf-8 -*-
"""
@author: Christian Charukiewicz (netid: charuki1)

This program converts an input matrix to Compressed Sparse Row (CSR) structure.

The last part of this program uses the scipy library to convert from CSR to LIL format.

More info: http://en.wikipedia.org/wiki/Sparse_matrix#Compressed_sparse_row_.28CSR_or_CRS.29

"""
import numpy
from scipy import *
from scipy.sparse import *

A = numpy.array([[11,0,0,0,0,0,14],
                 [0,0,0,0,24,0,0],
                 [0,0,0,0,33,34,0],
                 [0,15,0,0,43,44,0],
                 [0,0,0,0,0,54,0],
                 [0,0,62,0,0,0,0],
                 [0,0,72,0,0,0,0]])

print "=====INPUT MATRIX A====="
print A

AA = []
JA = []
IA = []

for i in range(0,7):
    for j in range(0,7):
        if (A[i][j] != 0):
            AA.append(A[i][j])
            JA.append(j+1)

IA.append(1)
for i in range(0,len(AA)-1):
    if(JA[i+1] <= JA[i]):
            IA.append(i+2)

IA.append(len(AA)+1)

print "=====OUTPUT====="
print "Vector AA:" , AA
print "Vector JA:" , JA
print "Vector IA:" , IA

JA = [i-1 for i in JA]
IA = [i-1 for i in IA]

AA = array(AA)
JA = array(JA)
IA = array(IA)

print " "
print "PART B"

matrix = scipy.sparse.csr_matrix((AA,JA,IA), shape=(7,7)).tolil()

print matrix
