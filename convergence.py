# -*- coding: utf-8 -*-
"""
@author: Christian Charukiewicz (netid: charuki1)

This compares the rates of convergence between the Newton and Secant methods.

The program will print output values and display a plot in matplotlib.

More info:
    - http://en.wikipedia.org/wiki/Newton's_method
    - http://en.wikipedia.org/wiki/Secant_method

"""
import numpy as np
import matplotlib.pyplot as plt
import math as mth

def f(x):
    return float((5-x)*mth.exp(x)-5)
    
def fd(x):
    return float(-1*mth.exp(x)*(x-4))

secx = []
secy = []
newx = []
newy = []

def secant(func, oldx, x):
    oldf, f = func(oldx), func(x)
    if (abs(f) > abs(oldf)):
        oldx, x = x, oldx
        oldf, f = f, oldf
    xk = 0
    while 1:
        dx = f * (x - oldx) / float(f - oldf)
        if abs(dx) < 10e-8 * (1 + abs(x)):
            return x - dx
        oldx, x = x, x - dx
        oldf, f = f, func(x)
        xk = xk + 1
        secx.append(xk)
        secy.append(mth.log(x))

def newton(f, fd, x):
    f_temp = f(x)
    fd_temp = fd(x)
    xk = 0
    while 1:
        dx = f_temp / float(fd_temp)
        if abs(dx) < 10e-8 * (1 + abs(x)):
            return x - dx
        x = x - dx
        f_temp = f(x)
        fd_temp = fd(x)
        xk = xk + 1
        newx.append(xk)
        newy.append(mth.log(x))
        

print "NEWTON's METHOD:" , newton(f, fd, 5)
print "SECANT METHOD:" , secant(f, 5, 10)
plt.plot(newx,newy,'r--',secx,secy,'b--')
plt.show()