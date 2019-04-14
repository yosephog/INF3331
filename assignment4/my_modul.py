import numpy as np
import matplotlib.pyplot as plt
import time
from numba import jit
import argparse

def compute(c,maxiter):

    z=0
    for i in range(maxiter):
        z=z**2 + c

        if abs(z) > 2:
            return i
    return 0

def mandel_python(xmin,xmax,ymin,ymax,width,height,maxiter):

    x=np.linspace(xmin,xmax,width)
    y=np.linspace(ymin,ymax,height)

    # creating a 2-dim array using only python
    list=[[0] * len(x) for lx in range(len(y))]

    for ii,i in enumerate(x):
        for jj,j in enumerate(y):
            list[ii][jj]=compute(complex(i,j),maxiter)
    return list

def mandel_numpy(xmin,xmax,ymin,ymax,width,height,maxiter):
    x=np.linspace(xmin,xmax,width)
    y=np.linspace(ymin,ymax,height)
    c=np.ravel(x + y[:,None]*1j)
    c=c.reshape((width,height))

    z=np.zeros((width,height))
    list=np.zeros((width,height))

    for i in range(maxiter):
        z=z*z + c
        isgreater=np.greater(abs(z),2.0)
        list=np.where(isgreater,i,list)
        z=np.where(isgreater,complex(0,0),z)
        c=np.where(isgreater,complex(0,0),c)

    return list

@jit(nopython=True)
def compute_numba(c,maxiter):

    z=0
    for i in range(maxiter):
        z=z**2 + c

        if abs(z) > 2:
            return i
    return 0
@jit(nopython=True)
def mandel_numba(xmin,xmax,ymin,ymax,width,height,maxiter):
    x=np.linspace(xmin,xmax,width)
    y=np.linspace(ymin,ymax,height)
    list=np.zeros((len(x),len(y)))
    for ii,i in enumerate(x):
        for jj,j in enumerate(y):
            list[ii][jj]=compute_numba(complex(i,j),maxiter)
    return list

def my_plotter(list,xmin,xmax,ymin,ymax):
    pass
